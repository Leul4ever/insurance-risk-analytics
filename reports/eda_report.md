# Exploratory Data Analysis (EDA) Report
## Insurance Risk Analytics - Task 1

**Date**: December 2025  
**Analyst**: Data Analytics Team  
**Dataset**: Insurance Claims Data (1,338 records)

---

## Executive Summary

This report presents a comprehensive exploratory data analysis of insurance data to understand risk patterns, identify key factors influencing charges, and uncover actionable insights for marketing strategy optimization. The analysis covers data quality assessment, statistical distributions, relationships between variables, geographic patterns, and risk segmentation.

### Key Findings

1. **Overall Portfolio**: 1,338 records with no missing values
2. **Mean Charges**: $13,270.42 (Median: $9,382.03)
3. **Charge Distribution**: Right-skewed with 10.39% outliers
4. **Geographic Variation**: Southeast region has highest mean charges ($14,735.41)
5. **Gender Difference**: Males have higher mean charges ($13,956.75) than females ($12,569.58)
6. **Risk Factors**: Age, BMI, and smoker status significantly impact charges

---

## 1. Data Overview

### 1.1 Dataset Structure

- **Total Records**: 1,338
- **Total Columns**: 7
- **Missing Values**: 0 (Complete dataset)
- **Duplicate Records**: 0

### 1.2 Column Information

| Column | Data Type | Description |
|--------|-----------|-------------|
| age | int64 | Age of the insured individual |
| sex | object | Gender (male/female) |
| bmi | float64 | Body Mass Index |
| children | int64 | Number of dependents |
| smoker | object | Smoking status (yes/no) |
| region | object | Geographic region (northeast/northwest/southeast/southwest) |
| charges | float64 | Individual medical costs billed by insurance |

---

## 2. Data Quality Assessment

### 2.1 Completeness
- ✅ **No missing values** detected across all columns
- ✅ **No duplicate records** found
- ✅ **Data types** are correctly formatted

### 2.2 Data Validation
- All numerical columns contain valid numeric values
- Categorical variables have consistent values
- No data range violations detected

---

## 3. Descriptive Statistics

### 3.1 Numerical Features Summary

| Statistic | age | bmi | children | charges |
|-----------|-----|-----|----------|---------|
| **Mean** | 39.21 | 30.66 | 1.09 | $13,270.42 |
| **Median** | 39.00 | 30.40 | 1.00 | $9,382.03 |
| **Std Dev** | 14.05 | 6.10 | 1.21 | $12,110.01 |
| **Min** | 18.00 | 15.96 | 0.00 | $1,121.87 |
| **Max** | 64.00 | 53.13 | 5.00 | $63,770.43 |
| **Q1** | 27.00 | 26.30 | 0.00 | $4,740.29 |
| **Q3** | 51.00 | 34.69 | 2.00 | $16,639.91 |
| **Skewness** | 0.06 | 0.28 | 0.94 | 1.52 |
| **Kurtosis** | -1.25 | 0.46 | 0.20 | 1.61 |

### 3.2 Key Observations

- **Charges**: Highly right-skewed distribution (skewness = 1.52), indicating most individuals have lower charges with a few high-cost outliers
- **Age**: Approximately normal distribution (skewness = 0.06)
- **BMI**: Slight right skew (skewness = 0.28), with mean near obesity threshold (30)
- **Children**: Right-skewed (skewness = 0.94), most individuals have 0-2 children

---

## 4. Univariate Analysis

### 4.1 Numerical Variables

#### Age Distribution
- Range: 18-64 years
- Mean: 39.21 years
- Distribution: Approximately normal
- **Insight**: Balanced age distribution across the portfolio

#### BMI Distribution
- Range: 15.96 - 53.13
- Mean: 30.66 (near obesity threshold of 30)
- **Insight**: Significant portion of individuals are overweight or obese

#### Charges Distribution
- Highly right-skewed
- Median ($9,382) significantly lower than mean ($13,270)
- **Insight**: Most individuals have moderate charges, but a small group drives up the average

### 4.2 Categorical Variables

#### Gender Distribution
- **Male**: 676 (50.5%)
- **Female**: 662 (49.5%)
- **Insight**: Balanced gender distribution

#### Smoker Status
- **Non-smokers**: 1,064 (79.5%)
- **Smokers**: 274 (20.5%)
- **Insight**: Majority are non-smokers, but smokers likely have higher charges

#### Regional Distribution
- **Southeast**: 364 (27.2%)
- **Southwest**: 325 (24.3%)
- **Northwest**: 325 (24.3%)
- **Northeast**: 324 (24.2%)
- **Insight**: Relatively balanced regional distribution

---

## 5. Bivariate and Multivariate Analysis

### 5.1 Correlation Analysis

| Variables | Correlation |
|-----------|-------------|
| age vs charges | 0.299 (Moderate positive) |
| bmi vs charges | 0.198 (Weak positive) |
| children vs charges | 0.068 (Very weak) |
| age vs bmi | 0.109 (Very weak) |

**Key Insights**:
- Age shows the strongest positive correlation with charges
- BMI has a moderate positive correlation
- Number of children has minimal impact on charges

### 5.2 Relationships

#### Age vs Charges
- Positive trend: Older individuals tend to have higher charges
- Scatter plot shows increasing charges with age, especially after 40

#### BMI vs Charges
- Weak positive relationship
- Higher BMI generally associated with higher charges
- Obesity threshold (BMI=30) appears to be a risk marker

---

## 6. Geographic and Demographic Analysis

### 6.1 Regional Analysis

| Region | Mean Charges | Median Charges | Count | Std Dev |
|--------|--------------|----------------|------|---------|
| **Southeast** | $14,735.41 | $9,294.13 | 364 | $13,971.10 |
| **Northeast** | $13,406.38 | $10,057.65 | 324 | $11,255.80 |
| **Northwest** | $12,417.58 | $8,965.80 | 325 | $11,072.28 |
| **Southwest** | $12,346.94 | $8,798.59 | 325 | $11,557.18 |

**Key Insights**:
- **Southeast** has the highest mean charges ($14,735.41), 11% above overall mean
- **Southwest** has the lowest mean charges ($12,346.94), 7% below overall mean
- Regional difference: $2,388.47 between highest and lowest

### 6.2 Gender Analysis

| Gender | Mean Charges | Median Charges | Count | Std Dev |
|--------|--------------|----------------|------|---------|
| **Male** | $13,956.75 | $9,369.62 | 676 | $12,971.03 |
| **Female** | $12,569.58 | $9,412.96 | 662 | $11,128.70 |

**Statistical Test**: Mann-Whitney U Test
- **Result**: Significant difference between genders (p < 0.05)
- **Insight**: Males have approximately 11% higher mean charges than females

---

## 7. Outlier Detection

### 7.1 Outlier Summary (IQR Method)

| Variable | Outlier Count | Outlier % | IQR | Lower Bound | Upper Bound |
|----------|---------------|-----------|-----|-------------|-------------|
| **age** | 0 | 0.00% | 24.00 | -9.00 | 87.00 |
| **bmi** | 9 | 0.67% | 8.40 | 13.70 | 47.29 |
| **children** | 0 | 0.00% | 2.00 | -3.00 | 5.00 |
| **charges** | 139 | 10.39% | $11,899.63 | -$13,109.15 | $34,489.35 |

### 7.2 Key Observations

- **Charges**: 139 outliers (10.39%) above $34,489.35
- **BMI**: 9 outliers (0.67%) above 47.29
- **Age & Children**: No outliers detected

**Recommendation**: High-charge outliers should be investigated separately as they may represent high-risk segments or data quality issues.

---

## 8. Answering Key Business Questions

### 8.1 Loss Ratio Analysis

**Note**: This dataset contains charges (medical costs) rather than separate claims and premiums. We analyze charges as the key financial metric.

#### Overall Portfolio Statistics
- **Total Charges**: $17,755,824.99
- **Mean Charges**: $13,270.42
- **Median Charges**: $9,382.03
- **Standard Deviation**: $12,110.01

#### Charges by Region (Relative to Overall Mean)

| Region | Mean Charges | Ratio to Overall |
|--------|--------------|------------------|
| Southeast | $14,735.41 | 1.110 (11% above) |
| Northeast | $13,406.38 | 1.010 (1% above) |
| Northwest | $12,417.58 | 0.936 (6% below) |
| Southwest | $12,346.94 | 0.930 (7% below) |

**Insight**: Southeast region shows significantly higher charges, suggesting potential regional risk factors.

#### Charges by Gender
- **Males**: $13,956.75 (1.05x overall mean)
- **Females**: $12,569.58 (0.95x overall mean)

**Insight**: Gender-based differences exist and should be considered in pricing models.

### 8.2 Temporal Trends

**Status**: No temporal columns (TransactionMonth, dates) found in this dataset.  
**Recommendation**: For temporal analysis, ensure transaction dates are included in future data collection.

### 8.3 Vehicle Analysis

**Status**: This dataset focuses on medical insurance rather than vehicle insurance.  
**Note**: For vehicle insurance analysis, columns like Make, Model, VehicleType would be required.

---

## 9. Creative Visualizations - Key Insights

### Visualization 1: Comprehensive Risk Profile (4-Panel Dashboard)

**Panels**:
1. **Charges by Region and Smoker Status**: Shows interaction between geographic location and smoking status
2. **Age vs Charges (colored by BMI)**: Reveals how age, BMI, and charges interact
3. **Mean Charges: Gender × Children**: Heatmap showing charge patterns across demographic combinations
4. **Cumulative Distribution**: Shows the distribution of charges with median and mean markers

**Key Insight**: Smoker status and region are major drivers of charges, with clear visual separation between risk groups.

### Visualization 2: Demographic Risk Patterns

**Components**:
- Violin plots showing charge distributions by region and smoker status
- Age distribution by smoker status
- BMI distribution with obesity threshold
- Summary statistics bar chart by region

**Key Insight**: Smokers consistently show higher charge distributions across all regions, with wider variance indicating higher risk.

### Visualization 3: Risk Segmentation Matrix (Improved with Color Bins)

**Components**:
1. **Risk Matrix (Age × BMI)**: Scatter plot with discrete charge level bins:
   - 🟢 **Green**: Very Low ($0-$5K)
   - 🟡 **Yellow**: Low ($5K-$10K)
   - 🟠 **Orange**: Medium ($10K-$20K)
   - 🔴 **Red**: High ($20K-$40K)
   - ⬛ **Dark Red**: Very High ($40K+)
2. **Charges by Number of Children**: Box plots showing distribution
3. **Regional Comparison**: Box plots with mean markers
4. **Risk Score Analysis**: Composite risk score based on smoker status and BMI

**Key Insight**: Clear visual risk segmentation - individuals with high BMI (>30) and older age show concentration of high-charge points (red/dark red). The discrete color bins make it immediately clear which individuals fall into high-risk categories.

---

## 10. Statistical Insights

### 10.1 Distribution Characteristics

- **Charges**: Non-normal, right-skewed distribution (skewness = 1.52)
- **Normality Test**: Charges do not follow normal distribution (p < 0.05)
- **Implication**: Non-parametric tests may be more appropriate for statistical analysis

### 10.2 Group Differences

#### Regional Differences
- **Highest**: Southeast ($14,735.41)
- **Lowest**: Southwest ($12,346.94)
- **Difference**: $2,388.47 (18% variation)

#### Gender Differences
- **Males**: $13,956.75
- **Females**: $12,569.58
- **Difference**: $1,387.17 (11% higher for males)
- **Statistical Significance**: Yes (Mann-Whitney U test, p < 0.05)

---

## 11. Key Insights and Recommendations

### 11.1 Risk Factors Identified

1. **High-Risk Segments**:
   - Smokers (20.5% of population)
   - Individuals with BMI > 30 (obesity threshold)
   - Older individuals (age > 50)
   - Southeast region residents

2. **Low-Risk Segments**:
   - Non-smokers
   - Normal BMI (< 25)
   - Younger individuals (age < 30)
   - Southwest region residents

### 11.2 Business Recommendations

1. **Premium Optimization**:
   - Consider higher premiums for Southeast region
   - Implement age-based pricing tiers
   - Adjust premiums based on BMI categories

2. **Marketing Strategy**:
   - Target low-risk segments (non-smokers, normal BMI, Southwest region) with competitive premiums
   - Develop wellness programs to reduce BMI-related risks
   - Focus on smoking cessation programs

3. **Risk Management**:
   - Monitor high-charge outliers (139 individuals, 10.39%)
   - Investigate factors driving Southeast region's higher charges
   - Develop predictive models using age, BMI, smoker status, and region

### 11.3 Data Quality Recommendations

1. **Future Data Collection**:
   - Include temporal columns (TransactionMonth) for trend analysis
   - Add vehicle-specific columns if analyzing auto insurance
   - Consider adding more granular geographic data (PostalCode)

2. **Outlier Handling**:
   - Investigate high-charge outliers separately
   - Consider separate models for high-risk vs. standard-risk segments

---

## 12. Conclusion

This exploratory data analysis has successfully identified key patterns and risk factors in the insurance portfolio:

- **Data Quality**: Excellent - no missing values, clean dataset
- **Key Drivers**: Age, BMI, smoker status, and region significantly impact charges
- **Risk Segmentation**: Clear high-risk and low-risk segments identified
- **Geographic Patterns**: Southeast region shows highest charges
- **Demographic Patterns**: Males and older individuals show higher charges

The analysis provides a solid foundation for:
- Predictive modeling (Task 3)
- A/B hypothesis testing (Task 2)
- Marketing strategy optimization
- Premium pricing models

**Next Steps**: Proceed to Task 2 (A/B Hypothesis Testing) and Task 3 (Machine Learning Models) based on these insights.

---

## Appendix

### A. Files Generated
- `notebooks/01_eda.ipynb` - Complete EDA notebook
- `reports/figures/` - All visualization files (11 figures)
- `src/data_loader.py` - Data loading utilities
- `src/eda_utils.py` - Statistical analysis functions
- `src/visualization.py` - Visualization functions

### B. Statistical Tests Performed
- Descriptive statistics (mean, median, std, quartiles, skewness, kurtosis)
- Correlation analysis
- Mann-Whitney U test (gender differences)
- Outlier detection (IQR method)
- Distribution normality tests

### C. Visualizations Created
1. Comprehensive Risk Profile (4-panel)
2. Demographic Risk Patterns (multi-panel)
3. Risk Segmentation Matrix (4-panel with improved color bins)

---

**Report Generated**: December 2025  
**Analysis Tool**: Python (pandas, numpy, matplotlib, seaborn, scipy)  
**Repository**: insurance-risk-analytics (task-1 branch)

