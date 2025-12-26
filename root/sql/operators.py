import inspect

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
operators_data = [
    # --- Math: Arithmetic ---
    {
        "operator_name": "add",
        "version": "0.0.1",
        "arity": 2,
        "category": "arithmetic",
        "description": "Поэлементное сложение двух датафреймов",
        "commutative": True,
        "associative": True,
        "idempotent": False
    },
    {
        "operator_name": "sub",
        "version": "0.0.1",
        "arity": 2,
        "category": "arithmetic",
        "description": "Поэлементное вычитание двух датафреймов",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "mul",
        "version": "0.0.1",
        "arity": 2,
        "category": "arithmetic",
        "description": "Поэлементное умножение двух датафреймов",
        "commutative": True,
        "associative": True,
        "idempotent": False
    },
    {
        "operator_name": "div",
        "version": "0.0.1",
        "arity": 2,
        "category": "arithmetic",
        "description": "Поэлементное деление двух датафреймов",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },

    # --- Math: Nonlinear ---
    {
        "operator_name": "power",
        "version": "0.0.1",
        "arity": 2,
        "category": "nonlinear",
        "description": "Поэлементное возведение в степень (x ^ v)",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "log1p",
        "version": "0.0.1",
        "arity": 1,
        "category": "nonlinear",
        "description": "Поэлементный натуральный логарифм от (1 + x)",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "abs",
        "version": "0.0.1",
        "arity": 1,
        "category": "nonlinear",
        "description": "Поэлементный модуль (абсолютное значение)",
        "commutative": False,
        "associative": False,
        "idempotent": True
    },
    {
        "operator_name": "sigmoid",
        "version": "0.0.1",
        "arity": 1,
        "category": "nonlinear",
        "description": "Поэлементная функция активации сигмоида",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "tanh",
        "version": "0.0.1",
        "arity": 1,
        "category": "nonlinear",
        "description": "Поэлементный гиперболический тангенс",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "relu",
        "version": "0.0.1",
        "arity": 1,
        "category": "nonlinear",
        "description": "Поэлементный ReLU (max(0, x))",
        "commutative": False,
        "associative": False,
        "idempotent": True
    },

    # --- Rolling: Moving Averages ---
    {
        "operator_name": "sma",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Простое скользящее среднее (SMA) с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "ema",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Экспоненциальное скользящее среднее (EMA) с коэффициентом затухания alpha",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_median",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящая медиана с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "savgol_smoothing",
        "version": "0.0.1",
        "arity": 3,
        "category": "rolling",
        "description": "Сглаживание фильтром Савицкого-Голея",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "wma",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Взвешенное скользящее среднее (WMA) с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "hull_moving_average",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящее среднее Хала (HMA) с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },

    # --- Rolling: Stats ---
    {
        "operator_name": "rolling_var",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящая дисперсия с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_std",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящее стандартное отклонение с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_skew",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящая асимметрия с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_kurt",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящий эксцесс с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },

    # --- Rolling: Other ---
    {
        "operator_name": "rolling_corr",
        "version": "0.0.1",
        "arity": 3,
        "category": "rolling",
        "description": "Скользящая корреляция между двумя датафреймами с окном w",
        "commutative": True,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_cov",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящая ковариация (или дисперсия для одного входа) с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_sum",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящая сумма с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_prod",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящее произведение с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_quadratic_variation",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящая квадратичная вариация с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },

    # --- Rolling: Sort Based ---
    {
        "operator_name": "rolling_max",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящий максимум с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_min",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящий минимум с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_rank",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящий ранг с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_argmin",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Индекс скользящего минимума с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_argmax",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Индекс скользящего максимума с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_quantile",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящий квантиль с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "rolling_deviance",
        "version": "0.0.1",
        "arity": 2,
        "category": "rolling",
        "description": "Скользящее отклонение (размах) с окном w",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },

    # --- Time Series ---
    {
        "operator_name": "diff",
        "version": "0.0.1",
        "arity": 2,
        "category": "timeseries",
        "description": "Дискретная разность элемента и элемента с лагом d",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "ts_variance_ratio",
        "version": "0.0.1",
        "arity": 2,
        "category": "timeseries",
        "description": "Тест отношения дисперсий временного ряда",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },

    # --- Logical ---
    {
        "operator_name": "greater_than",
        "version": "0.0.1",
        "arity": 2,
        "category": "logical",
        "description": "Поэлементное сравнение 'больше'",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "greater_equal",
        "version": "0.0.1",
        "arity": 2,
        "category": "logical",
        "description": "Поэлементное сравнение 'больше или равно'",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "lower_than",
        "version": "0.0.1",
        "arity": 2,
        "category": "logical",
        "description": "Поэлементное сравнение 'меньше'",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "lower_equal",
        "version": "0.0.1",
        "arity": 2,
        "category": "logical",
        "description": "Поэлементное сравнение 'меньше или равно'",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "equal",
        "version": "0.0.1",
        "arity": 2,
        "category": "logical",
        "description": "Поэлементное сравнение на равенство",
        "commutative": True,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "not_equal",
        "version": "0.0.1",
        "arity": 2,
        "category": "logical",
        "description": "Поэлементное сравнение на неравенство",
        "commutative": True,
        "associative": False,
        "idempotent": False
    },

    # --- Cross Sectional ---
    {
        "operator_name": "demean_cross_sectional",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Вычитание кросс-секционного среднего из элементов",
        "commutative": False,
        "associative": False,
        "idempotent": True
    },
    {
        "operator_name": "cs_mean",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Кросс-секционное среднее, распространенное (broadcasted) на форму данных",
        "commutative": False,
        "associative": False,
        "idempotent": True
    },
    {
        "operator_name": "cs_rank",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Кросс-секционный ранг",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_percentile",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Кросс-секционный процентильный ранг",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_zscore",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Кросс-секционная нормализация Z-score",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_range_normalize",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Кросс-секционная Min-Max нормализация",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_clip_outliers",
        "version": "0.0.1",
        "arity": 2,
        "category": "cross_sectional",
        "description": "Обрезание выбросов на основе кросс-секционного квантиля",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_divergence",
        "version": "0.0.1",
        "arity": 1,
        "category": "cross_sectional",
        "description": "Квадрат отклонения от кросс-секционного среднего",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_winsorize",
        "version": "0.0.1",
        "arity": 2,
        "category": "cross_sectional",
        "description": "Винзоризация данных на основе кросс-секционного квантиля",
        "commutative": False,
        "associative": False,
        "idempotent": False
    },
    {
        "operator_name": "cs_resid",
        "version": "0.0.1",
        "arity": 2,
        "category": "cross_sectional",
        "description": "Остатки кросс-секционной регрессии x на y",
        "commutative": False,
        "associative": False,
        "idempotent": False
    }
]
