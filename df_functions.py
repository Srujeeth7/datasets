import pandas as pd
import numpy as np

def get_columns_and_dtypes(df):
    column_info = pd.DataFrame({
        'Column Name': df.columns,
        'Data Type': df.dtypes.astype(str)
    })

    column_info.reset_index(drop=True, inplace=True)
    return column_info

def get_basic_details(df):
    details = {
        "Rows": df.shape[0],
        "Columns": df.shape[1]
    }
    return details

def calculate_additional_metrics(df):
    column_metrics = []
    for column in df.columns:
        null_pct = df[column].isnull().mean() * 100
        variance = df[column].var() if df[column].dtype in [np.float64, np.int64] else None
        info_value = np.nan  # Placeholder
        column_metrics.append({
            'Column Name': column,
            'Null Percentage': null_pct,
            'Variance': variance,
            'Information Value': info_value
        })
    return pd.DataFrame(column_metrics)

def get_file_details(df: pd.DataFrame, target_col: str):
    basic_details = get_basic_details(df)
    column_info = get_columns_and_dtypes(df)
    summary_df = df.describe().T
    summary_df = pd.merge(column_info, summary_df, right_index=True, left_on='Column Name', how='left')

    additional_metrics_df = calculate_additional_metrics(df)

    metrics_df = pd.merge(summary_df, additional_metrics_df, left_on='Column Name', right_on='Column Name', how='left')

    return basic_details, metrics_df