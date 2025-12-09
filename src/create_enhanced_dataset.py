"""
Script to create an enhanced insurance dataset with zip codes, TotalPremium, and TotalClaims.

This script enhances the existing insurance dataset by:
1. Adding zip codes based on regions
2. Splitting charges into TotalPremium and TotalClaims
3. Ensuring realistic relationships between variables
"""

import pandas as pd
import numpy as np
from pathlib import Path


def create_enhanced_dataset(input_file: str = "insurance.csv", output_file: str = "insurance_enhanced.csv"):
    """
    Create an enhanced dataset with zip codes, TotalPremium, and TotalClaims.
    
    Parameters:
    -----------
    input_file : str
        Name of the input CSV file
    output_file : str
        Name of the output CSV file
    """
    # Load original data
    data_path = Path(__file__).parent.parent / "data" / "raw" / input_file
    df = pd.read_csv(data_path)
    
    print(f"✓ Loaded original dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Create zip code mapping based on regions
    # South African postal codes (4-digit format)
    region_zip_mapping = {
        'northeast': [1000, 2000, 3000, 4000, 5000],  # Gauteng area
        'northwest': [2500, 2600, 2700, 2800, 2900],  # North West
        'southeast': [4000, 5000, 6000, 7000, 8000],  # KwaZulu-Natal/Eastern Cape
        'southwest': [7000, 8000, 9000, 10000, 11000]  # Western Cape
    }
    
    # Assign zip codes based on region with some variation
    np.random.seed(42)  # For reproducibility
    df['zipcode'] = df['region'].apply(
        lambda x: np.random.choice(region_zip_mapping[x])
    )
    
    # Add some random variation to zip codes (10% variation)
    variation_mask = np.random.random(len(df)) < 0.1
    df.loc[variation_mask, 'zipcode'] = df.loc[variation_mask, 'zipcode'] + np.random.randint(-500, 500, variation_mask.sum())
    df['zipcode'] = df['zipcode'].astype(int)
    
    # Create TotalPremium and TotalClaims from charges
    # Premium should be higher than claims (insurance companies need profit)
    # Loss ratio typically ranges from 0.6 to 0.9 (claims/premium)
    
    # Base premium calculation: charges * multiplier (premium is typically 1.2-1.5x charges)
    premium_multiplier = np.random.uniform(1.2, 1.5, len(df))
    df['TotalPremium'] = df['charges'] * premium_multiplier
    
    # Loss ratio varies by risk factors (smokers, age, BMI have higher loss ratios)
    base_loss_ratio = 0.65
    risk_adjustment = (
        (df['smoker'] == 'yes').astype(int) * 0.15 +  # Smokers: +15%
        (df['age'] > 50).astype(int) * 0.10 +  # Older: +10%
        (df['bmi'] > 30).astype(int) * 0.08 +  # High BMI: +8%
        np.random.normal(0, 0.05, len(df))  # Random variation
    )
    
    loss_ratio = np.clip(base_loss_ratio + risk_adjustment, 0.55, 0.90)
    df['TotalClaims'] = df['TotalPremium'] * loss_ratio
    
    # Ensure TotalClaims doesn't exceed TotalPremium
    df['TotalClaims'] = np.minimum(df['TotalClaims'], df['TotalPremium'] * 0.95)
    
    # Round to 2 decimal places
    df['TotalPremium'] = df['TotalPremium'].round(2)
    df['TotalClaims'] = df['TotalClaims'].round(2)
    
    # Calculate margin
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    
    # Reorder columns for better readability
    column_order = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'zipcode', 
                    'charges', 'TotalPremium', 'TotalClaims', 'Margin']
    df = df[column_order]
    
    # Save enhanced dataset
    output_path = Path(__file__).parent.parent / "data" / "raw" / output_file
    df.to_csv(output_path, index=False)
    
    print(f"✓ Created enhanced dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"✓ Saved to: {output_path}")
    print(f"\nNew columns added:")
    print(f"  - zipcode: {df['zipcode'].nunique()} unique zip codes")
    print(f"  - TotalPremium: Mean = ${df['TotalPremium'].mean():,.2f}")
    print(f"  - TotalClaims: Mean = ${df['TotalClaims'].mean():,.2f}")
    print(f"  - Margin: Mean = ${df['Margin'].mean():,.2f}")
    print(f"\nLoss Ratio (TotalClaims/TotalPremium): {df['TotalClaims'].sum() / df['TotalPremium'].sum():.2%}")
    
    return df


if __name__ == "__main__":
    create_enhanced_dataset()

