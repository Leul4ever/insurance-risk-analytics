"""
Exploratory Data Analysis utilities.

This module provides statistical analysis functions for EDA.
"""

from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy import stats


def calculate_descriptive_stats(
    df: pd.DataFrame, numeric_columns: List[str] = None
) -> pd.DataFrame:
    """
    Calculate comprehensive descriptive statistics for numerical columns.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_columns : List[str], optional
        List of numeric column names. If None, auto-detect numeric columns.

    Returns:
    --------
    pd.DataFrame
        Descriptive statistics including mean, median, std, min, max, quartiles, skewness, kurtosis
    """
    if numeric_columns is None:
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_columns:
        return pd.DataFrame()

    stats_dict = {
        "count": df[numeric_columns].count(),
        "mean": df[numeric_columns].mean(),
        "median": df[numeric_columns].median(),
        "std": df[numeric_columns].std(),
        "min": df[numeric_columns].min(),
        "max": df[numeric_columns].max(),
        "q25": df[numeric_columns].quantile(0.25),
        "q75": df[numeric_columns].quantile(0.75),
        "skewness": df[numeric_columns].skew(),
        "kurtosis": df[numeric_columns].kurtosis(),
        "variance": df[numeric_columns].var(),
    }

    return pd.DataFrame(stats_dict).T


def calculate_loss_ratio(
    df: pd.DataFrame, claims_col: str = "charges", premium_col: str = "charges"
) -> Dict:
    """
    Calculate loss ratio and variations.

    Note: For this dataset, we'll adapt based on available columns.
    Loss Ratio = TotalClaims / TotalPremium

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    claims_col : str
        Column name for claims/total charges
    premium_col : str
        Column name for premium/total charges

    Returns:
    --------
    dict
        Dictionary containing loss ratio calculations
    """
    # For this dataset, we'll calculate based on available columns
    # Adapting to work with charges as the main financial metric

    if claims_col not in df.columns or premium_col not in df.columns:
        # Fallback: use charges as both if columns don't exist
        if "charges" in df.columns:
            total_charges = df["charges"].sum()
            loss_ratio = {
                "overall_loss_ratio": 1.0,  # Placeholder - adapt based on actual data structure
                "total_charges": total_charges,
                "mean_charges": df["charges"].mean(),
                "median_charges": df["charges"].median(),
            }
        else:
            loss_ratio = {"error": "Required columns not found"}
    else:
        total_claims = df[claims_col].sum()
        total_premium = df[premium_col].sum()
        loss_ratio = {
            "overall_loss_ratio": (
                total_claims / total_premium if total_premium > 0 else 0
            ),
            "total_claims": total_claims,
            "total_premium": total_premium,
        }

    return loss_ratio


def calculate_loss_ratio_by_group(
    df: pd.DataFrame, group_col: str, value_col: str = "charges"
) -> pd.DataFrame:
    """
    Calculate loss ratio grouped by a categorical variable.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    group_col : str
        Column to group by
    value_col : str
        Column containing values to aggregate

    Returns:
    --------
    pd.DataFrame
        Grouped statistics
    """
    if group_col not in df.columns:
        return pd.DataFrame()

    grouped = (
        df.groupby(group_col)[value_col]
        .agg(["sum", "mean", "median", "count", "std"])
        .reset_index()
    )

    grouped.columns = [group_col, "total", "mean", "median", "count", "std"]
    return grouped


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> Tuple[pd.Series, Dict]:
    """
    Detect outliers using IQR method.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name to analyze

    Returns:
    --------
    Tuple[pd.Series, Dict]
        Boolean series indicating outliers and statistics dictionary
    """
    if column not in df.columns:
        return pd.Series(), {}

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = (df[column] < lower_bound) | (df[column] > upper_bound)

    stats_dict = {
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outlier_count": outliers.sum(),
        "outlier_percentage": (outliers.sum() / len(df)) * 100,
    }

    return outliers, stats_dict


def calculate_correlation_matrix(
    df: pd.DataFrame, numeric_columns: List[str] = None
) -> pd.DataFrame:
    """
    Calculate correlation matrix for numerical columns.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_columns : List[str], optional
        List of numeric column names. If None, auto-detect.

    Returns:
    --------
    pd.DataFrame
        Correlation matrix
    """
    if numeric_columns is None:
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_columns:
        return pd.DataFrame()

    return df[numeric_columns].corr()


def get_distribution_info(df: pd.DataFrame, column: str) -> Dict:
    """
    Get distribution information for a numerical column.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name to analyze

    Returns:
    --------
    dict
        Distribution statistics
    """
    if column not in df.columns:
        return {}

    data = df[column].dropna()

    # Test for normality
    stat, p_value = stats.normaltest(data)

    dist_info = {
        "mean": data.mean(),
        "median": data.median(),
        "mode": data.mode()[0] if len(data.mode()) > 0 else None,
        "std": data.std(),
        "skewness": data.skew(),
        "kurtosis": data.kurtosis(),
        "is_normal": p_value > 0.05,
        "normality_p_value": p_value,
    }

    return dist_info
