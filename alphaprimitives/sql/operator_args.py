import pandas as pd
from sqlalchemy import create_engine
operator_args_data = [
    # --- Math: Arithmetic ---
    {"operator_name": "add", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "add", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "sub", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "sub", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "mul", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "mul", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "div", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "div", "arg_name": "y", "position": 2, "data_type": "value"},

    # --- Math: Nonlinear ---
    {"operator_name": "power", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "power", "arg_name": "v", "position": 2, "data_type": "scalar"},

    {"operator_name": "log1p", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "abs", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "sigmoid", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "tanh", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "relu", "arg_name": "x", "position": 1, "data_type": "value"},

    # --- Rolling: Moving Averages ---
    {"operator_name": "sma", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "sma", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "ema", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "ema", "arg_name": "alpha", "position": 2, "data_type": "scalar", "min_value": 0.0001, "max_value": 0.9999},

    {"operator_name": "rolling_median", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_median", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "savgol_smoothing", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "savgol_smoothing", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 3},
    {"operator_name": "savgol_smoothing", "arg_name": "polyorder", "position": 3, "data_type": "scalar", "min_value": 1},

    {"operator_name": "wma", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "wma", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "hull_moving_average", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "hull_moving_average", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 5},

    # --- Rolling: Stats ---
    {"operator_name": "rolling_var", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_var", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_std", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_std", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_skew", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_skew", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 3},

    {"operator_name": "rolling_kurt", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_kurt", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 4},

    # --- Rolling: Other ---
    {"operator_name": "rolling_corr", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_corr", "arg_name": "y", "position": 2, "data_type": "value"},
    {"operator_name": "rolling_corr", "arg_name": "w", "position": 3, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_cov", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_cov", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_sum", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_sum", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_prod", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_prod", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_quadratic_variation", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_quadratic_variation", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    # --- Rolling: Sort Based ---
    {"operator_name": "rolling_max", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_max", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_min", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_min", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_rank", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_rank", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_argmin", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_argmin", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_argmax", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_argmax", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_quantile", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_quantile", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    {"operator_name": "rolling_deviance", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "rolling_deviance", "arg_name": "w", "position": 2, "data_type": "window", "min_value": 2},

    # --- Time Series ---
    {"operator_name": "diff", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "diff", "arg_name": "d", "position": 2, "data_type": "window", "min_value": 1},

    {"operator_name": "delay", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "delay", "arg_name": "d", "position": 2, "data_type": "window", "min_value": 1},

    # --- Logical ---
    {"operator_name": "greater_than", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "greater_than", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "greater_equal", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "greater_equal", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "lower_than", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "lower_than", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "lower_equal", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "lower_equal", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "equal", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "equal", "arg_name": "y", "position": 2, "data_type": "value"},

    {"operator_name": "not_equal", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "not_equal", "arg_name": "y", "position": 2, "data_type": "value"},

    # --- Cross Sectional ---
    {"operator_name": "demean_cross_sectional", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_mean", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_rank", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_percentile", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_zscore", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_range_normalize", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_divergence", "arg_name": "x", "position": 1, "data_type": "value"},

    {"operator_name": "cs_winsorize", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "cs_winsorize", "arg_name": "percentile", "position": 2, "data_type": "scalar", "min_value": 0.0, "max_value": 1.0},

    {"operator_name": "cs_resid", "arg_name": "x", "position": 1, "data_type": "value"},
    {"operator_name": "cs_resid", "arg_name": "y", "position": 2, "data_type": "value"},
]


def upload_df():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    df_args = pd.DataFrame.from_records(operator_args_data).assign(description="")
    df_operators = pd.read_sql_query(sql='select * from operators', con=engine)[['operator_id', 'operator_name']]
    df = df_operators.merge(df_args, on='operator_name', how='left').drop(columns=['operator_name'])
    df.to_sql(name='operator_args', con=engine, if_exists='append', index=False)

# upload_df()
