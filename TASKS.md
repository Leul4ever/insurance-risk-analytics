# Task 1: Git & GitHub + EDA & Statistics

## Overview
Set up version control, CI/CD pipeline, and perform comprehensive Exploratory Data Analysis (EDA) with statistical insights.

## 1.1 Git and GitHub

### Tasks
- [x] Create git repository with proper structure
- [x] Create README.md with project documentation
- [ ] Initialize git repository (`git init`)
- [ ] Create and switch to `task-1` branch
- [ ] Make initial commit with project structure
- [ ] Set up GitHub Actions CI/CD pipeline
- [ ] Commit work at least 3 times per day with descriptive messages

### Key Performance Indicators (KPIs)
- ✅ Dev Environment Setup
- ✅ Relevant skills demonstrated
- ✅ Proper git workflow and branching strategy

### GitHub Actions CI/CD
- [ ] Create workflow for code quality checks (linting)
- [ ] Create workflow for running tests
- [ ] Create workflow for notebook execution checks

## 1.2 Project Planning - EDA & Statistics

### Objective
Develop a foundational understanding of the data, assess its quality, and uncover initial patterns in risk and profitability.

### Tasks

#### Data Understanding
- [ ] Load and inspect the dataset
- [ ] Understand data structure and schema
- [ ] Document data dictionary

#### Exploratory Data Analysis (EDA)

##### Data Summarization
- [ ] **Descriptive Statistics**
  - Calculate variability for numerical features (TotalPremium, TotalClaims, etc.)
  - Compute mean, median, mode, std dev, min, max, quartiles
- [ ] **Data Structure**
  - Review dtype of each column
  - Confirm categorical variables, dates are properly formatted
  - Identify numerical vs categorical columns

##### Data Quality Assessment
- [ ] Check for missing values
  - Count missing values per column
  - Calculate percentage of missing data
  - Identify patterns in missing data
- [ ] Check for duplicates
- [ ] Validate data ranges and constraints

##### Univariate Analysis
- [ ] **Distribution of Variables**
  - Plot histograms for numerical columns
  - Plot bar charts for categorical columns
  - Identify distributions (normal, skewed, etc.)
  - Document key observations

##### Bivariate/Multivariate Analysis
- [ ] **Correlations and Associations**
  - Explore relationships between TotalPremium and TotalClaims
  - Analyze monthly changes in TotalPremium and TotalClaims
  - Create scatter plots
  - Build correlation matrices
  - Analyze relationships as a function of ZipCode

##### Data Comparison
- [ ] **Trends Over Geography**
  - Compare insurance cover type by location
  - Compare premium by location
  - Compare auto make/model by location
  - Visualize geographic patterns

##### Outlier Detection
- [ ] Use box plots to detect outliers in numerical data
  - TotalPremium outliers
  - TotalClaims outliers
  - CustomValueEstimate outliers
- [ ] Document outlier handling strategy

##### Visualization
- [ ] Produce **3 creative and beautiful plots** that capture key insights
  - Plot 1: [To be determined based on EDA]
  - Plot 2: [To be determined based on EDA]
  - Plot 3: [To be determined based on EDA]

### Guiding Questions to Answer

1. **Loss Ratio Analysis**
   - What is the overall Loss Ratio (TotalClaims / TotalPremium) for the portfolio?
   - How does Loss Ratio vary by Province?
   - How does Loss Ratio vary by VehicleType?
   - How does Loss Ratio vary by Gender?

2. **Financial Variable Distributions**
   - What are the distributions of key financial variables?
   - Are there outliers in TotalClaims that could skew analysis?
   - Are there outliers in CustomValueEstimate that could skew analysis?

3. **Temporal Trends**
   - Did claim frequency change over the 18-month period?
   - Did claim severity change over the 18-month period?
   - Are there seasonal patterns?

4. **Vehicle Analysis**
   - Which vehicle makes/models are associated with highest claim amounts?
   - Which vehicle makes/models are associated with lowest claim amounts?
   - What patterns exist in vehicle-related risk?

### Statistical Thinking

- [ ] Apply suitable statistical distributions
- [ ] Use appropriate statistical plots
- [ ] Provide evidence for actionable insights
- [ ] Demonstrate understanding of statistical concepts

### Key Performance Indicators (KPIs)

- ✅ Proactivity to self-learn - sharing references
- ✅ EDA techniques to understand data and discover insights
- ✅ Demonstrating Stats understanding using suitable distributions and plots
- ✅ Actionable insights gained from EDA

## Minimum Essential To Do Checklist

### Git & GitHub
- [x] Create GitHub repository
- [x] Create `task-1` branch
- [ ] Commit work at least 3 times per day with descriptive messages
- [ ] Set up CI/CD with GitHub Actions

### EDA Tasks
- [ ] Data Summarization (Descriptive Statistics & Data Structure)
- [ ] Data Quality Assessment (Missing Values)
- [ ] Univariate Analysis (Distributions)
- [ ] Bivariate/Multivariate Analysis (Correlations)
- [ ] Data Comparison (Geographic Trends)
- [ ] Outlier Detection (Box Plots)
- [ ] Create 3 Creative Visualizations

## Deliverables

1. **Git Repository**
   - Well-structured repository
   - Proper README.md
   - CI/CD pipeline

2. **EDA Notebook** (`notebooks/01_eda.ipynb`)
   - Complete exploratory analysis
   - All required visualizations
   - Statistical insights

3. **EDA Report** (`reports/eda_report.md`)
   - Summary of findings
   - Key insights
   - Visualizations embedded

4. **Source Code** (`src/`)
   - Modular functions for data loading
   - EDA utility functions
   - Visualization functions

5. **Figures** (`reports/figures/`)
   - All generated plots
   - High-quality visualizations

## Progress Tracking

**Started**: [Date]  
**Last Updated**: [Date]  
**Status**: In Progress

### Daily Commit Log
- [ ] Day 1: [Date] - [Description]
- [ ] Day 2: [Date] - [Description]
- [ ] Day 3: [Date] - [Description]


