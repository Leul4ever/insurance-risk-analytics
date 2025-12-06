"""
Hypothesis Testing utilities for A/B testing and statistical validation.

This module provides functions for conducting hypothesis tests on insurance data.
"""

from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats


def test_group_differences_anova(
    df: pd.DataFrame,
    group_column: str,
    metric_column: str,
    alpha: float = 0.05,
) -> Dict:
    """
    Test for differences across multiple groups using ANOVA.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    group_column : str
        Column name for grouping variable
    metric_column : str
        Column name for the metric to test
    alpha : float
        Significance level (default: 0.05)

    Returns:
    --------
    Dict
        Dictionary containing test results: statistic, p_value, reject_null, groups_stats
    """
    groups = [group[metric_column].values for name, group in df.groupby(group_column)]

    # Perform ANOVA
    f_statistic, p_value = stats.f_oneway(*groups)

    # Calculate group statistics
    group_stats = (
        df.groupby(group_column)[metric_column]
        .agg(["count", "mean", "median", "std"])
        .to_dict("index")
    )

    result = {
        "test": "ANOVA (F-test)",
        "null_hypothesis": f"No difference in {metric_column} across {group_column} groups",
        "f_statistic": f_statistic,
        "p_value": p_value,
        "alpha": alpha,
        "reject_null": p_value < alpha,
        "groups_stats": group_stats,
        "interpretation": (
            f"Reject H₀: There ARE significant differences"
            if p_value < alpha
            else f"Fail to reject H₀: No significant differences"
        ),
    }

    return result


def test_group_differences_mannwhitney(
    df: pd.DataFrame,
    group_column: str,
    metric_column: str,
    alpha: float = 0.05,
) -> Dict:
    """
    Test for differences between two groups using Mann-Whitney U test (non-parametric).

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    group_column : str
        Column name for grouping variable (must have exactly 2 groups)
    metric_column : str
        Column name for the metric to test
    alpha : float
        Significance level (default: 0.05)

    Returns:
    --------
    Dict
        Dictionary containing test results
    """
    groups = df.groupby(group_column)
    group_names = list(groups.groups.keys())

    if len(group_names) != 2:
        raise ValueError(
            f"Mann-Whitney U test requires exactly 2 groups. Found {len(group_names)} groups."
        )

    group1_data = groups.get_group(group_names[0])[metric_column].values
    group2_data = groups.get_group(group_names[1])[metric_column].values

    # Perform Mann-Whitney U test
    statistic, p_value = stats.mannwhitneyu(
        group1_data, group2_data, alternative="two-sided"
    )

    # Calculate group statistics
    group_stats = {
        group_names[0]: {
            "count": len(group1_data),
            "mean": np.mean(group1_data),
            "median": np.median(group1_data),
            "std": np.std(group1_data),
        },
        group_names[1]: {
            "count": len(group2_data),
            "mean": np.mean(group2_data),
            "median": np.median(group2_data),
            "std": np.std(group2_data),
        },
    }

    # Calculate difference
    mean_diff = (
        group_stats[group_names[0]]["mean"] - group_stats[group_names[1]]["mean"]
    )
    pct_diff = (mean_diff / group_stats[group_names[1]]["mean"]) * 100

    result = {
        "test": "Mann-Whitney U Test",
        "null_hypothesis": f"No difference in {metric_column} between {group_names[0]} and {group_names[1]}",
        "group1": group_names[0],
        "group2": group_names[1],
        "statistic": statistic,
        "p_value": p_value,
        "alpha": alpha,
        "reject_null": p_value < alpha,
        "mean_difference": mean_diff,
        "percent_difference": pct_diff,
        "groups_stats": group_stats,
        "interpretation": (
            f"Reject H₀: There IS a significant difference"
            if p_value < alpha
            else f"Fail to reject H₀: No significant difference"
        ),
    }

    return result


def test_group_differences_kruskal(
    df: pd.DataFrame,
    group_column: str,
    metric_column: str,
    alpha: float = 0.05,
) -> Dict:
    """
    Test for differences across multiple groups using Kruskal-Wallis test (non-parametric).

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    group_column : str
        Column name for grouping variable
    metric_column : str
        Column name for the metric to test
    alpha : float
        Significance level (default: 0.05)

    Returns:
    --------
    Dict
        Dictionary containing test results
    """
    groups = [group[metric_column].values for name, group in df.groupby(group_column)]

    # Perform Kruskal-Wallis test
    h_statistic, p_value = stats.kruskal(*groups)

    # Calculate group statistics
    group_stats = (
        df.groupby(group_column)[metric_column]
        .agg(["count", "mean", "median", "std"])
        .to_dict("index")
    )

    result = {
        "test": "Kruskal-Wallis Test",
        "null_hypothesis": f"No difference in {metric_column} across {group_column} groups",
        "h_statistic": h_statistic,
        "p_value": p_value,
        "alpha": alpha,
        "reject_null": p_value < alpha,
        "groups_stats": group_stats,
        "interpretation": (
            f"Reject H₀: There ARE significant differences"
            if p_value < alpha
            else f"Fail to reject H₀: No significant differences"
        ),
    }

    return result


def check_normality(data: np.ndarray, alpha: float = 0.05) -> Dict:
    """
    Check if data follows a normal distribution using Shapiro-Wilk test.

    Parameters:
    -----------
    data : np.ndarray
        Data to test
    alpha : float
        Significance level (default: 0.05)

    Returns:
    --------
    Dict
        Test results
    """
    # For large samples (>5000), use a sample
    if len(data) > 5000:
        data_sample = np.random.choice(data, size=5000, replace=False)
    else:
        data_sample = data

    statistic, p_value = stats.shapiro(data_sample)

    return {
        "test": "Shapiro-Wilk Test",
        "statistic": statistic,
        "p_value": p_value,
        "alpha": alpha,
        "is_normal": p_value >= alpha,
        "interpretation": (
            "Data appears normally distributed"
            if p_value >= alpha
            else "Data does NOT appear normally distributed"
        ),
    }


def calculate_effect_size_cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    """
    Calculate Cohen's d effect size for two groups.

    Parameters:
    -----------
    group1 : np.ndarray
        First group data
    group2 : np.ndarray
        Second group data

    Returns:
    --------
    float
        Cohen's d value
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    # Pooled standard deviation
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

    # Cohen's d
    d = (np.mean(group1) - np.mean(group2)) / pooled_std

    return d


def interpret_effect_size(d: float) -> str:
    """
    Interpret Cohen's d effect size.

    Parameters:
    -----------
    d : float
        Cohen's d value

    Returns:
    --------
    str
        Interpretation string
    """
    abs_d = abs(d)
    if abs_d < 0.2:
        return "negligible"
    elif abs_d < 0.5:
        return "small"
    elif abs_d < 0.8:
        return "medium"
    else:
        return "large"


def format_test_results(result: Dict) -> str:
    """
    Format test results as a readable string.

    Parameters:
    -----------
    result : Dict
        Test result dictionary

    Returns:
    --------
    str
        Formatted string
    """
    output = []
    output.append(f"\n{'='*60}")
    output.append(f"Test: {result['test']}")
    output.append(f"Null Hypothesis: {result['null_hypothesis']}")
    output.append(f"{'='*60}")

    if "f_statistic" in result:
        output.append(f"F-statistic: {result['f_statistic']:.4f}")
    elif "h_statistic" in result:
        output.append(f"H-statistic: {result['h_statistic']:.4f}")
    elif "statistic" in result:
        output.append(f"Test statistic: {result['statistic']:.4f}")

    output.append(f"P-value: {result['p_value']:.6f}")
    output.append(f"Alpha (significance level): {result['alpha']}")
    output.append(f"Decision: {result['interpretation']}")
    output.append(f"Reject H₀: {'Yes' if result['reject_null'] else 'No'}")

    if "mean_difference" in result:
        output.append(f"\nGroup Comparison:")
        output.append(f"  Mean Difference: ${result['mean_difference']:.2f}")
        output.append(f"  Percent Difference: {result['percent_difference']:.2f}%")

    if "groups_stats" in result:
        output.append(f"\nGroup Statistics:")
        for group, stats_dict in result["groups_stats"].items():
            output.append(f"\n  {group}:")
            for stat_name, stat_value in stats_dict.items():
                if isinstance(stat_value, float):
                    if stat_name in ["mean", "median", "std"]:
                        output.append(
                            f"    {stat_name.capitalize()}: ${stat_value:,.2f}"
                        )
                    else:
                        output.append(
                            f"    {stat_name.capitalize()}: {stat_value:,.2f}"
                        )
                else:
                    output.append(f"    {stat_name.capitalize()}: {stat_value}")

    output.append(f"{'='*60}\n")

    return "\n".join(output)
