import pandas as pd
from sqlalchemy import create_engine



operator_args_data = [
    {"operator_name": "add", "position": 1, "data_type": "value"},
    {"operator_name": "add", "position": 2, "data_type": "value"},

    {"operator_name": "sub", "position": 1, "data_type": "value"},
    {"operator_name": "sub", "position": 2, "data_type": "value"},

    {"operator_name": "mul", "position": 1, "data_type": "value"},
    {"operator_name": "mul", "position": 2, "data_type": "value"},

    {"operator_name": "div", "position": 1, "data_type": "value"},
    {"operator_name": "div", "position": 2, "data_type": "value"},

    # --- Math: Nonlinear ---
    {"operator_name": "power", "position": 1, "data_type": "value"},
    {"operator_name": "power", "position": 2, "data_type": "scalar"},

    {"operator_name": "log1p", "position": 1, "data_type": "value"},
    {"operator_name": "abs", "position": 1, "data_type": "value"},
    {"operator_name": "sigmoid", "position": 1, "data_type": "value"},
    {"operator_name": "tanh", "position": 1, "data_type": "value"},
    {"operator_name": "relu", "position": 1, "data_type": "value"},

    # --- Rolling: Moving Averages ---
    {"operator_name": "sma", "position": 1, "data_type": "value"},
    {"operator_name": "sma", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "ema", "position": 1, "data_type": "value"},
    {"operator_name": "ema", "position": 2, "data_type": "scalar", "min_value": 0.0001, "max_value": 0.9999},

    {"operator_name": "rolling_median", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_median", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "savgol_smoothing", "position": 1, "data_type": "value"},
    {"operator_name": "savgol_smoothing", "position": 2, "data_type": "window", "min_value": 3},
    {"operator_name": "savgol_smoothing", "position": 3, "data_type": "scalar", "min_value": 1},

    {"operator_name": "wma", "position": 1, "data_type": "value"},
    {"operator_name": "wma", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "hull_moving_average", "position": 1, "data_type": "value"},
    {"operator_name": "hull_moving_average", "position": 2, "data_type": "window", "min_value": 5},

    # --- Rolling: Stats ---
    {"operator_name": "rolling_var", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_var", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_std", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_std", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_skew", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_skew", "position": 2, "data_type": "window", "min_value": 3},

    {"operator_name": "rolling_kurt", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_kurt", "position": 2, "data_type": "window", "min_value": 4},

    # --- Rolling: Other ---
    {"operator_name": "rolling_corr", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_corr", "position": 2, "data_type": "value"},
    {"operator_name": "rolling_corr", "position": 3, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_cov", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_cov", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_sum", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_sum", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_prod", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_prod", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_quadratic_variation", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_quadratic_variation", "position": 2, "data_type": "window", "min_value": 2},

    # --- Rolling: Sort Based ---
    {"operator_name": "rolling_max", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_max", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_min", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_min", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_rank", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_rank", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_argmin", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_argmin", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_argmax", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_argmax", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_quantile", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_quantile", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_deviance", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_deviance", "position": 2, "data_type": "window", "min_value": 2},

    # --- Time Series ---
    {"operator_name": "diff", "position": 1, "data_type": "value"},
    {"operator_name": "diff", "position": 2, "data_type": "window", "min_value": 1},

    {"operator_name": "ts_variance_ratio", "position": 1, "data_type": "value"},
    {"operator_name": "ts_variance_ratio", "position": 2, "data_type": "window", "min_value": 2},

    # --- Logical ---
    {"operator_name": "greater_than", "position": 1, "data_type": "value"},
    {"operator_name": "greater_than", "position": 2, "data_type": "value"},

    {"operator_name": "greater_equal", "position": 1, "data_type": "value"},
    {"operator_name": "greater_equal", "position": 2, "data_type": "value"},

    {"operator_name": "lower_than", "position": 1, "data_type": "value"},
    {"operator_name": "lower_than", "position": 2, "data_type": "value"},

    {"operator_name": "lower_equal", "position": 1, "data_type": "value"},
    {"operator_name": "lower_equal", "position": 2, "data_type": "value"},

    {"operator_name": "equal", "position": 1, "data_type": "value"},
    {"operator_name": "equal", "position": 2, "data_type": "value"},

    {"operator_name": "not_equal", "position": 1, "data_type": "value"},
    {"operator_name": "not_equal", "position": 2, "data_type": "value"},

    # --- Cross Sectional ---
    {"operator_name": "demean_cross_sectional", "position": 1, "data_type": "value"},

    {"operator_name": "cs_mean", "position": 1, "data_type": "value"},

    {"operator_name": "cs_rank", "position": 1, "data_type": "value"},

    {"operator_name": "cs_percentile", "position": 1, "data_type": "value"},

    {"operator_name": "cs_zscore", "position": 1, "data_type": "value"},

    {"operator_name": "cs_range_normalize", "position": 1, "data_type": "value"},

    {"operator_name": "cs_divergence", "position": 1, "data_type": "value"},

    {"operator_name": "cs_winsorize", "position": 1, "data_type": "value"},
    {"operator_name": "cs_winsorize", "position": 2, "data_type": "scalar", "min_value": 0.0, "max_value": 0.5},

    {"operator_name": "cs_resid", "position": 1, "data_type": "value"},
    {"operator_name": "cs_resid", "position": 2, "data_type": "value"},

]

def upload_df():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    df_args = pd.DataFrame.from_records(operator_args_data).assign(description="")
    df_operators = pd.read_sql_query(sql='select * from operators', con=engine)[['operator_id', 'operator_name']]
    df = df_operators.merge(df_args, on='operator_name', how='left').drop(columns=['operator_name'])
    df.to_sql(name='operator_args', con=engine, if_exists='append', index=False)

# upload_df()
