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
├── .dvc/                  # DVC configuration and cache
├── .github/
│   └── workflows/        # CI/CD pipelines
├── data/
│   ├── raw/              # Original data (tracked by DVC)
│   └── processed/        # Cleaned data
├── notebooks/
│   ├── 01_eda.ipynb      # EDA notebook
│   └── 02_preprocessing.ipynb
├── reports/
│   ├── figures/          # Visualization files (11 figures)
│   └── eda_report.md     # Comprehensive EDA report
├── src/
│   ├── __init__.py
│   ├── data_loader.py    # Data loading utilities
│   ├── eda_utils.py      # Statistical analysis functions
│   └── visualization.py  # Plotting functions
├── tests/
├── dvc_storage/          # DVC local storage (data files)
├── requirements.txt
├── README.md
├── INTERIM_REPORT.md     # Interim submission report
├── .gitignore
└── LICENSE
```

## Key Deliverables

### Task 1: Git & GitHub + EDA & Statistics ✅
- [x] Git repository setup with proper structure
- [x] Comprehensive README documentation
- [x] CI/CD pipeline with GitHub Actions
- [x] Exploratory Data Analysis (EDA)
- [x] Statistical analysis and visualizations
- [x] EDA report with key insights
- [x] 3 creative visualizations
- [x] Complete descriptive statistics
- [x] Geographic and demographic analysis

### Task 2: Data Version Control (DVC) ✅
- [x] DVC installation and initialization
- [x] Local remote storage configuration
- [x] Data files added to DVC tracking
- [x] DVC metadata files committed to Git
- [x] Data pushed to local storage
- [x] Reproducible data pipeline established
- [x] DVC workflow documented

### Task 3: A/B Hypothesis Testing ✅
- [x] Test risk differences across provinces (regions)
- [x] Test risk differences between zipcodes
- [x] Test margin (profit) differences between zip codes
- [x] Test risk differences between Women and men
- [x] Statistical test reports

### Task 4: Machine Learning & Predictive Modeling
- [ ] Linear regression models per zipcode (predicting total claims)
- [ ] ML model for optimal premium prediction
- [ ] Feature importance analysis
- [ ] Model evaluation and validation

### Final Deliverable
- [ ] Comprehensive report detailing methodologies
- [ ] Findings and recommendations
- [ ] Plan features modification suggestions

## Data Description

**Time Period**: Historical insurance data (1,338 records)

**Current Dataset Structure**:
- **Demographics**: Age, Gender (sex), BMI, Number of children
- **Behavioral**: Smoker status
- **Geographic**: Region (northeast, northwest, southeast, southwest)
- **Financial**: Charges (insurance costs)

**Note**: The current dataset contains insurance charges as the primary financial metric. For a complete insurance analysis, the following categories would be included:

**Expected Data Categories** (for full analysis):
- **Policy Information**: UnderwrittenCoverID, PolicyID, TransactionMonth
- **Client Demographics**: Gender, MaritalStatus, Citizenship, LegalType, Title, Language
- **Location**: Country, Province, PostalCode, MainCrestaZone, SubCrestaZone
- **Vehicle Details**: Make, Model, RegistrationYear, VehicleType, Bodytype, etc.
- **Plan Details**: SumInsured, Premium, CoverType, CoverCategory, etc.
- **Financial**: TotalPremium, TotalClaims

**Data Versioning**: All data files are tracked using DVC (Data Version Control) for reproducibility and auditability.

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
- DVC (Data Version Control) - installed via requirements.txt

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

# Pull data from DVC (if data files are not present)
python -m dvc pull
```

### Data Access

**Using DVC**:
```bash
# Check DVC status
python -m dvc status

# Pull data files
python -m dvc pull

# View tracked files
python -m dvc list data/raw/
```

**Data Location**:
- Raw data: `data/raw/insurance.csv` (tracked by DVC)
- Processed data: `data/processed/` (for cleaned/transformed data)
- DVC storage: `dvc_storage/` (local remote storage)

## Key Dates

- **Challenge Introduction**: 10:30 AM UTC, Wednesday, 03 Dec 2025
- **Interim Submission**: 8:00 PM UTC, Sunday, 07 Dec 2025
- **Final Submission**: 8:00 PM UTC, Tuesday, 09 Dec 2025

## Learning Outcomes

- **Data Engineering (DE)**: Data pipeline setup, EDA, data quality assessment
- **Predictive Analytics (PA)**: Statistical analysis, hypothesis testing, predictive modeling
- **Machine Learning Engineering (MLE)**: Model development, feature engineering, model evaluation
- **Statistical Modeling and Analysis**: Descriptive statistics, correlation analysis, distribution analysis
- **A/B Testing Design and Implementation**: Hypothesis testing, statistical significance testing
- **Data Versioning**: DVC setup, reproducible data pipelines, audit trails
- **Modular and Object-Oriented Python**: Clean code structure, reusable functions, best practices
- **Version Control**: Git workflows, CI/CD pipelines, collaborative development

## Team

- Facilitator: Kerod
- Facilitator: Mahbubah
- Facilitator: Filimon

## Project Status

### Completed Tasks
- ✅ **Task 1**: Git & GitHub + EDA & Statistics
- ✅ **Task 2**: Data Version Control (DVC)

### Completed
- ✅ **Task 3**: A/B Hypothesis Testing

### Upcoming
- ⏳ **Task 4**: Machine Learning & Predictive Modeling

### Reports
- **Interim Report**: `INTERIM_REPORT.md` - Covers Tasks 1 & 2
- **EDA Report**: `reports/eda_report.md` - Comprehensive EDA findings
- **Hypothesis Testing Report**: `reports/hypothesis_testing_report.md` - Complete A/B testing results
- **Task Summaries**: `TASK1_COMPLETION_SUMMARY.md`, `TASK2_COMPLETION_SUMMARY.md`, `TASK3_COMPLETION_SUMMARY.md`

## Repository Links

- **GitHub Repository**: [insurance-risk-analytics](https://github.com/Leul4ever/insurance-risk-analytics)
- **Main Branch**: Contains merged work from task-1 and task-2
- **Active Branches**: task-1, task-2

## License

See LICENSE file for details.


