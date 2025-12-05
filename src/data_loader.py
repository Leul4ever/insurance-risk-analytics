"""
Data loading utilities for insurance risk analytics.

This module provides functions to load and perform basic operations on insurance data.
"""

import pandas as pd
import os
from pathlib import Path


def get_data_path(filename: str, data_type: str = "raw") -> Path:
    """
    Get the full path to a data file.

    Parameters:
    -----------
    filename : str
        Name of the data file (e.g., 'insurance.csv')
    data_type : str
        Type of data directory: 'raw' or 'processed'

    Returns:
    --------
    Path
        Full path to the data file
    """
    project_root = Path(__file__).parent.parent
    data_path = project_root / "data" / data_type / filename
    return data_path


def load_insurance_data(
    filename: str = "insurance.csv", data_type: str = "raw"
) -> pd.DataFrame:
    """
    Load insurance data from CSV file.

    Parameters:
    -----------
    filename : str
        Name of the CSV file to load
    data_type : str
        Type of data directory: 'raw' or 'processed'

    Returns:
    --------
    pd.DataFrame
        Loaded insurance data
    """
    file_path = get_data_path(filename, data_type)

    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    df = pd.read_csv(file_path)
    return df


def get_data_info(df: pd.DataFrame) -> dict:
    """
    Get basic information about the dataset.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    dict
        Dictionary containing dataset information
    """
    info = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.to_dict(),
        "memory_usage": df.memory_usage(deep=True).sum(),
        "missing_values": df.isnull().sum().to_dict(),
        "missing_percentage": (df.isnull().sum() / len(df) * 100).to_dict(),
        "duplicates": df.duplicated().sum(),
    }
    return info


def validate_data(df: pd.DataFrame) -> dict:
    """
    Validate data quality and return validation results.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    dict
        Dictionary containing validation results
    """
    validation = {
        "has_missing": df.isnull().any().any(),
        "has_duplicates": df.duplicated().any(),
        "empty_dataframe": df.empty,
        "numeric_columns": df.select_dtypes(include=["number"]).columns.tolist(),
        "categorical_columns": df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist(),
    }
    return validation
