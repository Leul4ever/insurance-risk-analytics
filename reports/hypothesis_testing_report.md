# Hypothesis Testing Report
## A/B Testing - Task 3
## Insurance Risk Analytics

**Date**: December 2025  
**Analyst**: Data Analytics Team  
**Dataset**: Insurance Claims Data (1,338 records)

---

## Executive Summary

This report presents the results of statistical hypothesis testing to validate or reject key hypotheses about risk drivers in insurance data. The analysis tests risk differences across geographic regions and between genders, providing actionable insights for pricing strategy and risk management.

### Key Findings

1. **Regional Risk Differences**: ❌ **FAIL TO REJECT H₀** (p = 0.192) - No significant risk differences across regions
2. **Gender Risk Differences**: ❌ **FAIL TO REJECT H₀** (p = 0.729) - No significant risk differences between genders
3. **Zip Code Analysis**: ❌ **Cannot test** - Missing zip code data
4. **Margin Analysis**: ❌ **Cannot test** - Missing separate premium/claims data

---

## 1. Methodology

### 1.1 Data Overview

- **Total Records**: 1,338
- **Risk Metric**: Charges (used as proxy for risk, since separate claim frequency/severity not available)
- **Geographic Variable**: Region (northeast, northwest, southeast, southwest)
- **Demographic Variable**: Gender (male, female)

### 1.2 Statistical Tests

**Test Selection Criteria**:
- Data distribution checked using Shapiro-Wilk test
- Since data is **not normally distributed** (right-skewed), **non-parametric tests** were used:
  - **Kruskal-Wallis Test**: For comparing multiple groups (regions)
  - **Mann-Whitney U Test**: For comparing two groups (genders)

**Significance Level**: α = 0.05

### 1.3 Data Limitations

**Missing Data**:
- ❌ Zip codes/Postal codes - Cannot test zip code hypotheses
- ❌ Separate TotalPremium/TotalClaims columns - Cannot calculate margin
- ❌ Claim frequency indicators - Cannot calculate claim frequency/severity separately

**Adaptations**:
- Used **regions** instead of provinces (4 regions available)
- Used **charges** as proxy for risk (combined metric)
- Documented limitations clearly in results

---

## 2. Hypothesis Testing Results

### Hypothesis 1: Risk Differences Across Regions (Provinces)

**H₀**: There are no risk differences across regions (provinces)  
**H₁**: There are significant risk differences across regions

**Test**: Kruskal-Wallis Test (non-parametric ANOVA)

**Results**:

| Region | Count | Mean Charges | Median Charges | Std Dev |
|--------|-------|-------------|----------------|---------|
| **Southeast** | 364 | $14,735.41 | $9,294.13 | $13,971.10 |
| **Northeast** | 324 | $13,406.38 | $10,057.65 | $11,255.80 |
| **Northwest** | 325 | $12,417.58 | $8,965.80 | $11,072.28 |
| **Southwest** | 325 | $12,346.94 | $8,798.59 | $11,557.18 |

**Test Statistics**:
- **H-statistic**: 4.7342
- **P-value**: 0.192329
- **Decision**: **FAIL TO REJECT H₀** (p ≥ 0.05)

**Interpretation**:
- **No significant regional differences detected** (p = 0.192). While Southeast region shows the highest mean charges ($14,735.41) compared to Southwest ($12,346.94), representing a 19.3% difference, this difference is **not statistically significant** at the 0.05 level.
- **Business Implication**: Uniform pricing across regions may be appropriate. The observed differences are likely due to random variation rather than systematic regional risk factors.

**Pairwise Comparisons** (if H₀ rejected):
- Post-hoc Mann-Whitney U tests between all region pairs
- Identifies which specific regions differ significantly

---

### Hypothesis 2: Risk Differences Between Genders

**H₀**: There is no significant risk difference between Women and Men  
**H₁**: There is a significant risk difference between Women and Men

**Test**: Mann-Whitney U Test (non-parametric two-sample test)

**Results**:

| Gender | Count | Mean Charges | Median Charges | Std Dev |
|--------|-------|-------------|----------------|---------|
| **Male** | 676 | $13,956.75 | $9,369.62 | $12,971.03 |
| **Female** | 662 | $12,569.58 | $9,412.96 | $11,128.70 |

**Test Statistics**:
- **Test Statistic**: 225,000+ (Mann-Whitney U)
- **P-value**: 0.728651
- **Mean Difference**: $1,387.17 (males higher)
- **Percent Difference**: 11.0% (males higher)
- **Effect Size (Cohen's d)**: 0.1147 (negligible effect)
- **Decision**: **FAIL TO REJECT H₀** (p ≥ 0.05)

**Interpretation**:
- **No significant gender difference detected** (p = 0.729). While males show an 11% higher mean charges ($13,956.75 vs $12,569.58), this difference is **not statistically significant**.
- **Effect Size**: Cohen's d = 0.1147 indicates a **negligible effect size**, further supporting that gender is not a meaningful risk factor.
- **Business Implication**: Gender-neutral pricing is statistically justified. The observed difference is likely due to random variation or confounding factors (e.g., age, BMI, smoking status) rather than gender itself.

---

### Hypothesis 3: Risk Differences Between Zip Codes

**H₀**: There are no risk differences between zip codes  
**H₁**: There are significant risk differences between zip codes

**Status**: ❌ **CANNOT TEST**

**Reason**: Zip code/postal code column is not available in the dataset. Only region-level data is available.

**Recommendation**: Collect zip code data for granular geographic analysis.

---

### Hypothesis 4: Margin Differences Between Zip Codes

**H₀**: There is no significant margin (profit) difference between zip codes  
**H₁**: There is a significant margin difference between zip codes

**Status**: ❌ **CANNOT TEST**

**Reasons**:
1. Zip code/postal code column is not available
2. Separate TotalPremium and TotalClaims columns are not available
3. Margin = TotalPremium - TotalClaims cannot be calculated

**Recommendation**: 
- Collect zip code data
- Separate premium and claims data to enable margin analysis

---

## 3. Summary Table

| Hypothesis | Test | P-value | Decision | Status |
|------------|------|---------|----------|--------|
| H₀: No risk differences across regions | Kruskal-Wallis | 0.192329 | Fail to reject H₀ | ✅ Tested |
| H₀: No risk differences between zip codes | N/A | N/A | Cannot test - missing data | ❌ Cannot test |
| H₀: No margin difference between zip codes | N/A | N/A | Cannot test - missing data | ❌ Cannot test |
| H₀: No risk difference between Women and Men | Mann-Whitney U | 0.728651 | Fail to reject H₀ | ✅ Tested |

---

## 4. Business Recommendations

### 4.1 Regional Risk Adjustment

**Finding**: **No significant regional differences** (p = 0.192, Fail to reject H₀)

**Statistical Result**: 
- Kruskal-Wallis Test: H-statistic = 4.7342, p-value = 0.192329
- While Southeast region shows 19.3% higher mean charges than Southwest ($14,735.41 vs $12,346.94), this difference is **not statistically significant** at α = 0.05

**Business Recommendation**:
1. **Uniform Pricing Strategy**:
   - **No regional risk adjustment is warranted** based on current statistical evidence
   - Maintain uniform pricing across all regions to simplify operations and ensure fairness
   - The observed differences (Southeast 19.3% higher than Southwest) are likely due to random variation rather than systematic regional risk factors

2. **Ongoing Monitoring**:
   - Continue monitoring regional trends quarterly
   - If future data shows emerging patterns, re-evaluate pricing strategy
   - Consider collecting more granular geographic data (zip codes) for deeper analysis

3. **Business Interpretation**: 
   "We fail to reject the null hypothesis for regional differences (p = 0.192). While Southeast exhibits 19.3% higher charges than Southwest ($14,735 vs $12,347), this difference is not statistically significant. **Uniform pricing across regions is statistically justified and operationally simpler.**"

---

### 4.2 Gender-Based Risk

**Finding**: **No significant gender differences** (p = 0.729, Fail to reject H₀)

**Statistical Result**:
- Mann-Whitney U Test: p-value = 0.728651
- Mean difference: $1,387.17 (males 11% higher)
- Effect size (Cohen's d): 0.1147 (negligible effect)

**Business Recommendation**:
1. **Gender-Neutral Pricing**:
   - **No gender-based pricing adjustment is warranted** based on statistical evidence
   - Gender-neutral pricing is statistically justified and aligns with anti-discrimination best practices
   - The observed 11% difference is not statistically significant and has a negligible effect size

2. **Regulatory Compliance**:
   - Gender-neutral pricing is recommended regardless of statistical findings
   - Many jurisdictions prohibit or restrict gender-based pricing in insurance
   - Focus on other risk factors (age, BMI, smoking status) that show stronger statistical significance

3. **Business Interpretation**:
   "We fail to reject the null hypothesis for gender differences (p = 0.729). While males exhibit 11% higher charges than females ($13,957 vs $12,570), this difference is not statistically significant and has a negligible effect size (Cohen's d = 0.115). **Gender-neutral pricing is both statistically justified and aligned with regulatory best practices.**"

---

### 4.3 Data Collection Recommendations

To enable complete hypothesis testing as specified in the requirements:

1. **Geographic Data**:
   - ✅ Region (available)
   - ❌ Province (use region as proxy)
   - ❌ PostalCode/ZipCode (needed for granular analysis)

2. **Financial Data**:
   - ❌ TotalPremium (premiums collected)
   - ❌ TotalClaims (claims paid)
   - ✅ Charges (available, but combined metric)

3. **Policy Data**:
   - ❌ PolicyID (to track individual policies)
   - ❌ TransactionMonth (for temporal analysis)
   - ❌ Claim indicators (binary: claim occurred or not)

4. **Metrics to Calculate**:
   - Loss Ratio = TotalClaims / TotalPremium
   - Margin = TotalPremium - TotalClaims
   - Claim Frequency = Number of claims / Number of policies
   - Claim Severity = Average claim amount

---

## 5. Statistical Rigor

### 5.1 Test Assumptions

**Kruskal-Wallis Test**:
- ✅ Independent samples
- ✅ Ordinal or continuous data
- ✅ No assumption of normality (non-parametric)

**Mann-Whitney U Test**:
- ✅ Independent samples
- ✅ Ordinal or continuous data
- ✅ No assumption of normality (non-parametric)

### 5.2 Effect Size

Effect sizes (Cohen's d) calculated for gender comparison:
- **Interpretation**:
  - |d| < 0.2: Negligible effect
  - 0.2 ≤ |d| < 0.5: Small effect
  - 0.5 ≤ |d| < 0.8: Medium effect
  - |d| ≥ 0.8: Large effect

### 5.3 Multiple Comparisons

For regional analysis with multiple groups:
- Post-hoc pairwise comparisons conducted if H₀ is rejected
- Bonferroni correction or similar adjustment may be applied for multiple comparisons

---

## 6. Limitations

1. **Data Limitations**:
   - Missing zip code data prevents granular geographic analysis
   - Missing separate premium/claims data prevents margin analysis
   - Charges used as proxy for risk (not ideal, but necessary given data constraints)

2. **Statistical Limitations**:
   - Non-parametric tests used (less powerful than parametric tests, but appropriate for non-normal data)
   - Effect sizes should be interpreted alongside p-values

3. **Business Context**:
   - Regulatory compliance must be considered for gender-based pricing
   - Regional pricing adjustments must align with business strategy
   - Additional factors (age, BMI, smoking status) may confound results

---

## 7. Next Steps

1. **Data Collection**:
   - Collect zip code data for granular analysis
   - Separate premium and claims data
   - Include temporal data for trend analysis

2. **Further Analysis**:
   - Multivariate analysis controlling for confounding factors
   - Interaction effects (e.g., region × gender)
   - Temporal trends if data becomes available

3. **Implementation**:
   - Review regulatory requirements
   - Develop pricing models based on findings
   - Monitor and validate pricing adjustments

---

## Appendix

### A. Test Code Location

- **Notebook**: `notebooks/03_hypothesis_testing.ipynb`
- **Module**: `src/hypothesis_testing.py`
- **Visualizations**: `reports/figures/hypothesis_testing_*.png`

### B. Statistical Test References

- Kruskal-Wallis Test: Non-parametric alternative to one-way ANOVA
- Mann-Whitney U Test: Non-parametric alternative to independent samples t-test
- Cohen's d: Effect size measure for comparing two groups

---

**Report Prepared By**: Data Analytics Team  
**Date**: December 2025  
**Submission**: Task 3 - A/B Hypothesis Testing  
**Next Review**: Task 4 (Machine Learning & Predictive Modeling)

---

*This report covers the hypothesis testing requirements for Task 3. All statistical tests have been conducted with appropriate rigor, and limitations have been clearly documented.*

