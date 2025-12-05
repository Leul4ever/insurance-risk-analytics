"""
Visualization utilities for insurance risk analytics.

This module provides functions for creating publication-quality plots.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, List, Tuple


# Set style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 10


def save_figure(fig, filename: str, dpi: int = 300, bbox_inches: str = "tight"):
    """
    Save figure to reports/figures directory.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        Figure object to save
    filename : str
        Name of the output file
    dpi : int
        Resolution for saved figure
    bbox_inches : str
        Bounding box setting
    """
    project_root = Path(__file__).parent.parent
    figures_dir = project_root / "reports" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    filepath = figures_dir / filename
    fig.savefig(filepath, dpi=dpi, bbox_inches=bbox_inches)
    print(f"Figure saved to: {filepath}")


def plot_distribution(
    df: pd.DataFrame,
    column: str,
    figsize: Tuple[int, int] = (10, 6),
    save: bool = False,
    filename: Optional[str] = None,
) -> plt.Figure:
    """
    Plot distribution of a numerical column (histogram + KDE).

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name to plot
    figsize : Tuple[int, int]
        Figure size
    save : bool
        Whether to save the figure
    filename : str, optional
        Filename for saving

    Returns:
    --------
    matplotlib.figure.Figure
        Figure object
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # Histogram with KDE
    sns.histplot(data=df, x=column, kde=True, ax=axes[0])
    axes[0].set_title(f"Distribution of {column}")
    axes[0].set_xlabel(column)
    axes[0].set_ylabel("Frequency")

    # Box plot
    sns.boxplot(data=df, y=column, ax=axes[1])
    axes[1].set_title(f"Box Plot of {column}")
    axes[1].set_ylabel(column)

    plt.tight_layout()

    if save:
        if filename is None:
            filename = f"distribution_{column}.png"
        save_figure(fig, filename)

    return fig


def plot_categorical_counts(
    df: pd.DataFrame,
    column: str,
    figsize: Tuple[int, int] = (10, 6),
    save: bool = False,
    filename: Optional[str] = None,
) -> plt.Figure:
    """
    Plot bar chart for categorical column.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name to plot
    figsize : Tuple[int, int]
        Figure size
    save : bool
        Whether to save the figure
    filename : str, optional
        Filename for saving

    Returns:
    --------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)

    value_counts = df[column].value_counts()
    sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax, palette="viridis")
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    if save:
        if filename is None:
            filename = f"categorical_{column}.png"
        save_figure(fig, filename)

    return fig


def plot_correlation_heatmap(
    df: pd.DataFrame,
    numeric_columns: List[str] = None,
    figsize: Tuple[int, int] = (12, 10),
    save: bool = False,
    filename: str = "correlation_heatmap.png",
) -> plt.Figure:
    """
    Plot correlation heatmap for numerical columns.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_columns : List[str], optional
        List of numeric columns. If None, auto-detect.
    figsize : Tuple[int, int]
        Figure size
    save : bool
        Whether to save the figure
    filename : str
        Filename for saving

    Returns:
    --------
    matplotlib.figure.Figure
        Figure object
    """
    if numeric_columns is None:
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_columns:
        raise ValueError("No numeric columns found")

    fig, ax = plt.subplots(figsize=figsize)

    corr_matrix = df[numeric_columns].corr()
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.8},
        ax=ax,
    )
    ax.set_title("Correlation Heatmap", fontsize=14, fontweight="bold")

    plt.tight_layout()

    if save:
        save_figure(fig, filename)

    return fig


def plot_boxplot_by_group(
    df: pd.DataFrame,
    numeric_col: str,
    group_col: str,
    figsize: Tuple[int, int] = (12, 6),
    save: bool = False,
    filename: Optional[str] = None,
) -> plt.Figure:
    """
    Plot box plots grouped by a categorical variable.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_col : str
        Numerical column to plot
    group_col : str
        Categorical column to group by
    figsize : Tuple[int, int]
        Figure size
    save : bool
        Whether to save the figure
    filename : str, optional
        Filename for saving

    Returns:
    --------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)

    sns.boxplot(data=df, x=group_col, y=numeric_col, ax=ax, palette="Set2")
    ax.set_title(f"{numeric_col} by {group_col}", fontsize=14, fontweight="bold")
    ax.set_xlabel(group_col)
    ax.set_ylabel(numeric_col)
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    if save:
        if filename is None:
            filename = f"boxplot_{numeric_col}_by_{group_col}.png"
        save_figure(fig, filename)

    return fig


def plot_scatter_with_trend(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    group_col: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    save: bool = False,
    filename: Optional[str] = None,
) -> plt.Figure:
    """
    Plot scatter plot with trend line.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    x_col : str
        X-axis column
    y_col : str
        Y-axis column
    group_col : str, optional
        Column to color-code by
    figsize : Tuple[int, int]
        Figure size
    save : bool
        Whether to save the figure
    filename : str, optional
        Filename for saving

    Returns:
    --------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)

    if group_col:
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=group_col, ax=ax, alpha=0.6)
        sns.regplot(data=df, x=x_col, y=y_col, scatter=False, ax=ax, color="red")
    else:
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax, alpha=0.6)
        sns.regplot(data=df, x=x_col, y=y_col, scatter=False, ax=ax, color="red")

    ax.set_title(f"{y_col} vs {x_col}", fontsize=14, fontweight="bold")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    plt.tight_layout()

    if save:
        if filename is None:
            filename = f"scatter_{x_col}_vs_{y_col}.png"
        save_figure(fig, filename)

    return fig
