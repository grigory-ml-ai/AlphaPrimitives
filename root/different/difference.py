import pandas as pd
import bottleneck as bn

#TODO: построить проверку. Задержка должна быть корректной
def diff(x: pd.DataFrame, d: int) -> pd.DataFrame:
    return x - x.shift(d)

def ts_variance_ratio(x: pd.DataFrame, w: int) -> pd.DataFrame:
    bn.move_var(x.values, )