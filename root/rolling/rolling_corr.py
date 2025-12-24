import numpy as np
import pandas as pd
from numba import njit, prange


@njit(cache=True, fastmath=False)
def _rolling_corr_vec_numba(x: np.ndarray, y: np.ndarray, window: int, min_periods=None):
    n = x.shape[0]
    out = np.full(n, np.nan)
    if min_periods is None:
        min_periods = window

    sum_x = 0.0
    sum_y = 0.0
    sum_x2 = 0.0
    sum_y2 = 0.0
    sum_xy = 0.0
    m = 0

    # Буферы для удаления вкладов при сдвиге окна
    buf_x = np.empty(window)
    buf_y = np.empty(window)
    buf_isvalid = np.empty(window, dtype=np.uint8)
    head = 0  # позиция для записи в кольцевом буфере (0..window-1), соответствует "новому" элементу

    for i in range(n):
        xi = x[i]
        yi = y[i]
        # Проверка на NaN (xi == xi быстрее np.isnan в некоторых случаях для скаляров)
        is_valid = (not np.isnan(xi)) and (not np.isnan(yi))

        # Если окно уже заполнено, вычесть вклад уходящего элемента
        if i >= window:
            tail = head  # элемент, который выйдет
            if buf_isvalid[tail] == 1:
                x_old = buf_x[tail]
                y_old = buf_y[tail]
                sum_x -= x_old
                sum_y -= y_old
                sum_x2 -= x_old * x_old
                sum_y2 -= y_old * y_old
                sum_xy -= x_old * y_old
                m -= 1

        # Добавить новый элемент
        if is_valid:
            sum_x += xi
            sum_y += yi
            sum_x2 += xi * xi
            sum_y2 += yi * yi
            sum_xy += xi * yi
            m += 1
            buf_x[head] = xi
            buf_y[head] = yi
            buf_isvalid[head] = 1
        else:
            # Заполняем, чтобы корректно вычесть позже
            buf_x[head] = 0.0
            buf_y[head] = 0.0
            buf_isvalid[head] = 0

        # Сдвиг головки буфера
        head += 1
        if head == window:
            head = 0

        # Вычисление корреляции
        # Исправление: убрана проверка if i >= window - 1, чтобы считать на растущем окне,
        # если набралось достаточно валидных точек (m >= min_periods)
        if m >= min_periods and m >= 2:
            denom_x = (sum_x2 - (sum_x * sum_x) / m)
            denom_y = (sum_y2 - (sum_y * sum_y) / m)

            # Защита от отрицательной дисперсии из-за ошибок округления float
            if denom_x < 0: denom_x = 0.0
            if denom_y < 0: denom_y = 0.0

            denom = np.sqrt(denom_x * denom_y)
            num = (sum_xy - (sum_x * sum_y) / m)

            if denom > 1e-14:
                out[i] = num / denom
            else:
                out[i] = np.nan
        # else: остается np.nan, инициализированный в начале

    return out


@njit(cache=True, parallel=True)
def _column_wise_apply(x: np.ndarray, y: np.ndarray, w: int) -> np.ndarray:
    n_rows, n_cols = x.shape
    out = np.empty_like(x, dtype=x.dtype)
    for col in prange(n_cols):
        out[:, col] = _rolling_corr_vec_numba(x[:, col], y[:, col], w)
    return out


def rolling_corr(x: pd.DataFrame, y: pd.DataFrame, w: int) -> pd.DataFrame:
    out = _column_wise_apply(x.values, y.values, w)
    return pd.DataFrame(out, index=x.index, columns=x.columns)
