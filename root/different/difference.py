import pandas as pd


# TODO: построить проверку. Задержка должна быть корректной
def diff(x: pd.DataFrame, d: int) -> pd.DataFrame:
    if d <= 1:
        raise RuntimeError(f'Error at diff function. Delay value must be greater than 1. Got: {d}')
    return x - x.shift(d)


def delay(x: pd.DataFrame, d: int) -> pd.DataFrame:
    if d <= 1:
        raise RuntimeError(f'Error at shift function. Delay value must be greater than 1. Got: {d}')
    return x.shift(d)
