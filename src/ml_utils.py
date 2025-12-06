"""
Machine Learning utilities for insurance risk analytics.

This module provides functions for data preprocessing, model training,
evaluation, and interpretability analysis.
"""

from typing import Dict, List, Tuple, Optional, Any

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    mean_absolute_error,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
import xgboost as xgb
import shap


def prepare_features(
    df: pd.DataFrame,
    categorical_cols: List[str],
    numerical_cols: List[str],
    target_col: str,
    test_size: float = 0.2,
    random_state: int = 42,
    encode_method: str = "onehot",
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series, Dict]:
    """
    Prepare features for machine learning.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    categorical_cols : List[str]
        List of categorical column names
    numerical_cols : List[str]
        List of numerical column names
    target_col : str
        Name of target variable column
    test_size : float
        Proportion of data for testing (default: 0.2)
    random_state : int
        Random seed for reproducibility
    encode_method : str
        Encoding method: 'onehot' or 'label' (default: 'onehot')

    Returns:
    --------
    Tuple
        X_train, X_test, y_train, y_test, feature_names, encoders_dict
    """
    # Create a copy to avoid modifying original
    df_processed = df.copy()

    # Separate features and target
    X = df_processed[numerical_cols + categorical_cols].copy()
    y = df_processed[target_col].copy()

    # Encode categorical variables
    encoders = {}
    feature_names = numerical_cols.copy()

    if encode_method == "onehot":
        # One-hot encoding
        ohe = OneHotEncoder(drop="first", sparse_output=False)
        for col in categorical_cols:
            if col in X.columns:
                encoded = ohe.fit_transform(X[[col]])
                encoded_df = pd.DataFrame(
                    encoded,
                    columns=[f"{col}_{cat}" for cat in ohe.categories_[0][1:]],
                    index=X.index,
                )
                X = pd.concat([X.drop(columns=[col]), encoded_df], axis=1)
                feature_names.extend(encoded_df.columns.tolist())
                encoders[col] = ohe
    else:
        # Label encoding
        for col in categorical_cols:
            if col in X.columns:
                le = LabelEncoder()
                X[col] = le.fit_transform(X[col])
                encoders[col] = le

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test, feature_names, encoders


def train_linear_regression(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Tuple[LinearRegression, Dict]:
    """
    Train a linear regression model.

    Parameters:
    -----------
    X_train : pd.DataFrame
        Training features
    y_train : pd.Series
        Training target
    X_test : pd.DataFrame
        Test features
    y_test : pd.Series
        Test target

    Returns:
    --------
    Tuple
        Trained model and evaluation metrics
    """
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluation metrics
    metrics = {
        "train_rmse": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "test_rmse": np.sqrt(mean_squared_error(y_test, y_test_pred)),
        "train_r2": r2_score(y_train, y_train_pred),
        "test_r2": r2_score(y_test, y_test_pred),
        "train_mae": mean_absolute_error(y_train, y_train_pred),
        "test_mae": mean_absolute_error(y_test, y_test_pred),
    }

    return model, metrics


def train_decision_tree(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    max_depth: Optional[int] = None,
    min_samples_split: int = 2,
) -> Tuple[DecisionTreeRegressor, Dict]:
    """
    Train a decision tree regressor.

    Parameters:
    -----------
    X_train : pd.DataFrame
        Training features
    y_train : pd.Series
        Training target
    X_test : pd.DataFrame
        Test features
    y_test : pd.Series
        Test target
    max_depth : Optional[int]
        Maximum tree depth
    min_samples_split : int
        Minimum samples to split

    Returns:
    --------
    Tuple
        Trained model and evaluation metrics
    """
    # Train model
    model = DecisionTreeRegressor(
        max_depth=max_depth, min_samples_split=min_samples_split, random_state=42
    )
    model.fit(X_train, y_train)

    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluation metrics
    metrics = {
        "train_rmse": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "test_rmse": np.sqrt(mean_squared_error(y_test, y_test_pred)),
        "train_r2": r2_score(y_train, y_train_pred),
        "test_r2": r2_score(y_test, y_test_pred),
        "train_mae": mean_absolute_error(y_train, y_train_pred),
        "test_mae": mean_absolute_error(y_test, y_test_pred),
    }

    return model, metrics


def train_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    n_estimators: int = 100,
    max_depth: Optional[int] = None,
    random_state: int = 42,
) -> Tuple[RandomForestRegressor, Dict]:
    """
    Train a random forest regressor.

    Parameters:
    -----------
    X_train : pd.DataFrame
        Training features
    y_train : pd.Series
        Training target
    X_test : pd.DataFrame
        Test features
    y_test : pd.Series
        Test target
    n_estimators : int
        Number of trees
    max_depth : Optional[int]
        Maximum tree depth
    random_state : int
        Random seed

    Returns:
    --------
    Tuple
        Trained model and evaluation metrics
    """
    # Train model
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluation metrics
    metrics = {
        "train_rmse": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "test_rmse": np.sqrt(mean_squared_error(y_test, y_test_pred)),
        "train_r2": r2_score(y_train, y_train_pred),
        "test_r2": r2_score(y_test, y_test_pred),
        "train_mae": mean_absolute_error(y_train, y_train_pred),
        "test_mae": mean_absolute_error(y_test, y_test_pred),
    }

    return model, metrics


def train_xgboost(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    n_estimators: int = 100,
    max_depth: int = 6,
    learning_rate: float = 0.1,
    random_state: int = 42,
) -> Tuple[xgb.XGBRegressor, Dict]:
    """
    Train an XGBoost regressor.

    Parameters:
    -----------
    X_train : pd.DataFrame
        Training features
    y_train : pd.Series
        Training target
    X_test : pd.DataFrame
        Test features
    y_test : pd.Series
        Test target
    n_estimators : int
        Number of boosting rounds
    max_depth : int
        Maximum tree depth
    learning_rate : float
        Learning rate
    random_state : int
        Random seed

    Returns:
    --------
    Tuple
        Trained model and evaluation metrics
    """
    # Train model
    model = xgb.XGBRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=learning_rate,
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluation metrics
    metrics = {
        "train_rmse": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "test_rmse": np.sqrt(mean_squared_error(y_test, y_test_pred)),
        "train_r2": r2_score(y_train, y_train_pred),
        "test_r2": r2_score(y_test, y_test_pred),
        "train_mae": mean_absolute_error(y_train, y_train_pred),
        "test_mae": mean_absolute_error(y_test, y_test_pred),
    }

    return model, metrics


def get_feature_importance(
    model: Any, feature_names: List[str], top_n: int = 10
) -> pd.DataFrame:
    """
    Get feature importance from a trained model.

    Parameters:
    -----------
    model : Any
        Trained model with feature_importances_ attribute
    feature_names : List[str]
        List of feature names
    top_n : int
        Number of top features to return

    Returns:
    --------
    pd.DataFrame
        DataFrame with feature names and importance scores
    """
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
    elif hasattr(model, "coef_"):
        # For linear models, use absolute coefficients
        importances = np.abs(model.coef_)
    else:
        raise ValueError("Model does not have feature_importances_ or coef_")

    # Create DataFrame
    importance_df = pd.DataFrame(
        {"feature": feature_names, "importance": importances}
    ).sort_values("importance", ascending=False)

    return importance_df.head(top_n)


def calculate_shap_values(
    model: Any, X_sample: pd.DataFrame, max_samples: int = 100
) -> Tuple[Any, Any]:
    """
    Calculate SHAP values for model interpretability.

    Parameters:
    -----------
    model : Any
        Trained model
    X_sample : pd.DataFrame
        Sample data for SHAP calculation
    max_samples : int
        Maximum number of samples to use (for performance)

    Returns:
    --------
    Tuple
        SHAP values and SHAP explainer object
    """
    # Sample data if too large
    if len(X_sample) > max_samples:
        X_sample = X_sample.sample(n=max_samples, random_state=42)

    # Create SHAP explainer based on model type
    try:
        if isinstance(model, (xgb.XGBRegressor, xgb.XGBClassifier)):
            explainer = shap.TreeExplainer(model)
        elif isinstance(model, (RandomForestRegressor, RandomForestClassifier, DecisionTreeRegressor)):
            explainer = shap.TreeExplainer(model)
        elif hasattr(model, 'coef_'):
            # For linear models, use LinearExplainer
            explainer = shap.LinearExplainer(model, X_sample)
        else:
            # Fallback to KernelExplainer for other models
            explainer = shap.KernelExplainer(model.predict, X_sample)
        
        # Calculate SHAP values
        shap_values = explainer.shap_values(X_sample)
        
        return shap_values, explainer
    except Exception as e:
        raise ValueError(f"Error creating SHAP explainer: {e}. Model type may not be supported.")


def compare_models(model_results: Dict[str, Dict]) -> pd.DataFrame:
    """
    Compare multiple models' performance.

    Parameters:
    -----------
    model_results : Dict[str, Dict]
        Dictionary with model names as keys and metrics as values

    Returns:
    --------
    pd.DataFrame
        Comparison table
    """
    comparison_data = []
    for model_name, metrics in model_results.items():
        comparison_data.append(
            {
                "Model": model_name,
                "Test RMSE": metrics.get("test_rmse", np.nan),
                "Test R²": metrics.get("test_r2", np.nan),
                "Test MAE": metrics.get("test_mae", np.nan),
                "Train RMSE": metrics.get("train_rmse", np.nan),
                "Train R²": metrics.get("train_r2", np.nan),
            }
        )

    comparison_df = pd.DataFrame(comparison_data)
    return comparison_df.sort_values("Test RMSE")


def create_claim_indicator(df: pd.DataFrame, charges_col: str = "charges") -> pd.DataFrame:
    """
    Create a binary claim indicator based on charges.

    Since we don't have explicit claim data, we'll create a synthetic
    claim indicator where claims > 0 if charges exceed a threshold.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    charges_col : str
        Name of charges column

    Returns:
    --------
    pd.DataFrame
        Dataframe with 'has_claim' column added
    """
    df_copy = df.copy()
    
    # Create claim indicator: 1 if charges > median, 0 otherwise
    # This simulates a scenario where higher charges indicate claims occurred
    median_charges = df_copy[charges_col].median()
    df_copy["has_claim"] = (df_copy[charges_col] > median_charges).astype(int)
    
    return df_copy

