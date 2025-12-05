# Insurance Risk Analytics & Predictive Modeling

## Project Overview

**Company**: AlphaCare Insurance Solutions (ACIS)  
**Role**: Marketing Analytics Engineer  
**Objective**: Analyze historical insurance claim data to optimize marketing strategy and discover "low-risk" targets for premium reduction, creating opportunities to attract new clients.

## Business Objective

Develop cutting-edge risk and predictive analytics for car insurance planning and marketing in South Africa. The analysis aims to:
- Optimize marketing strategy
- Discover "low-risk" segments for premium reduction
- Attract new clients through data-driven insights

## Project Structure

```
insurance-risk-analytics/
├── data/
│   ├── raw/              # Original data
│   └── processed/        # Cleaned data
├── notebooks/
│   ├── 01_eda.ipynb      # EDA notebook
│   └── 02_preprocessing.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   └── visualization.py
├── reports/
│   ├── figures/          # Save plots here
│   └── eda_report.md
├── tests/
├── .github/
│   └── workflows/        # CI/CD pipelines
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Key Deliverables

### Task 1: Git & GitHub + EDA & Statistics
- [x] Git repository setup with proper structure
- [ ] Comprehensive README documentation
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Exploratory Data Analysis (EDA)
- [ ] Statistical analysis and visualizations
- [ ] EDA report with key insights

### Task 2: A/B Hypothesis Testing
- [ ] Test risk differences across provinces
- [ ] Test risk differences between zipcodes
- [ ] Test margin (profit) differences between zip codes
- [ ] Test risk differences between Women and men
- [ ] Statistical test reports

### Task 3: Machine Learning & Predictive Modeling
- [ ] Linear regression models per zipcode (predicting total claims)
- [ ] ML model for optimal premium prediction
- [ ] Feature importance analysis
- [ ] Model evaluation and validation

### Final Deliverable
- [ ] Comprehensive report detailing methodologies
- [ ] Findings and recommendations
- [ ] Plan features modification suggestions

## Data Description

**Time Period**: February 2014 to August 2015 (18 months)

**Data Categories**:
- **Policy Information**: UnderwrittenCoverID, PolicyID, TransactionMonth
- **Client Demographics**: Gender, MaritalStatus, Citizenship, LegalType, Title, Language
- **Location**: Country, Province, PostalCode, MainCrestaZone, SubCrestaZone
- **Vehicle Details**: Make, Model, RegistrationYear, VehicleType, Bodytype, etc.
- **Plan Details**: SumInsured, Premium, CoverType, CoverCategory, etc.
- **Financial**: TotalPremium, TotalClaims

## Key Metrics

- **Loss Ratio**: TotalClaims / TotalPremium
- **Claim Frequency**: Number of claims per policy
- **Claim Severity**: Average claim amount
- **Profit Margin**: Premium - Claims

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- Jupyter Notebook

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd insurance-risk-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Key Dates

- **Challenge Introduction**: 10:30 AM UTC, Wednesday, 03 Dec 2025
- **Interim Submission**: 8:00 PM UTC, Sunday, 07 Dec 2025
- **Final Submission**: 8:00 PM UTC, Tuesday, 09 Dec 2025

## Learning Outcomes

- Data Engineering (DE)
- Predictive Analytics (PA)
- Machine Learning Engineering (MLE)
- Statistical Modeling and Analysis
- A/B Testing Design and Implementation
- Data Versioning
- Modular and Object-Oriented Python

## Team

- Facilitator: Kerod
- Facilitator: Mahbubah
- Facilitator: Filimon

## License

See LICENSE file for details.


