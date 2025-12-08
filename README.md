# Insurance Risk Analytics & Predictive Modeling

End-to-end analytics pipeline for insurance risk and pricing across four tasks: EDA, DVC, hypothesis testing, and machine learning models (severity, premium, claim probability) with interpretability and business recommendations.

## Project Snapshot
- **Company (fictional)**: AlphaCare Insurance Solutions (ACIS)
- **Scope**: Risk analytics, hypothesis testing, and ML-driven pricing
- **Data**: 1,338 policies; demographics (age, sex), BMI, children, smoker, region, charges
- **Branch**: `main` (tasks 1–4 merged)

## What’s Done (Tasks 1–4)
- **Task 1 – EDA & Statistics**
  - Full EDA notebook (`notebooks/01_eda.ipynb`) with descriptive stats, outliers, correlations, and 3 creative visualizations; EDA report in `reports/eda_report.md`.
  - CI/CD via GitHub Actions; repo structure, gitignore, requirements, setup docs.
- **Task 2 – DVC**
  - DVC initialized; `data/raw/insurance.csv` tracked via `.dvc` and stored in `dvc_storage/`; usage documented in `SETUP.md`.
- **Task 3 – Hypothesis Testing**
  - Kruskal–Wallis across regions; Mann–Whitney U for gender. Both fail to reject H₀ (no significant differences); documented limitations for missing zip/premium/claims fields.
  - Notebook `notebooks/03_hypothesis_testing.ipynb`; report `reports/hypothesis_testing_report.md`; figures in `reports/figures/`.
- **Task 4 – Machine Learning & Pricing**
  - Claim severity (charges | has_claim=1): Linear/DecisionTree/RandomForest/XGBoost with RMSE, R², MAE.
  - Premium prediction (charges all): same regressors and metrics.
  - Claim probability: Logistic/DecisionTree/RandomForest/XGBoost classifiers with accuracy/precision/recall/F1.
  - Risk-based premium framing: premium ≈ P(claim) × severity + loading + margin.
  - Feature engineering: age_squared, BMI category, age groups, has_claim; one-hot encoding; 80/20 split.
  - Interpretability: SHAP (top drivers include smoker, BMI, age); feature importance utilities; plots in `reports/figures/`.

## Repository Structure
```
insurance-risk-analytics/
├── .github/workflows/ci.yml     # CI checks (lint/format/notebook validation)
├── .dvc/                        # DVC config
├── data/
│   ├── raw/insurance.csv.dvc    # Raw data pointer (tracked by DVC)
│   └── processed/               # Derived data (if generated)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb   # Scaffold
│   ├── 03_hypothesis_testing.ipynb
│   └── 04_ml_modeling.ipynb
├── reports/
│   ├── figures/                 # EDA, hypothesis tests, ML, SHAP
│   ├── eda_report.md
│   ├── hypothesis_testing_report.md
│   └── INTERIM_REPORT.md
├── src/
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_testing.py
│   ├── ml_utils.py              # Prep, models, metrics, SHAP
│   └── visualization.py
├── requirements.txt
├── TASK1_COMPLETION_SUMMARY.md
├── TASK2_COMPLETION_SUMMARY.md
├── TASK3_COMPLETION_SUMMARY.md
├── TASK4_VERIFICATION.md
├── DELIVERABLES.md
├── SETUP.md
└── README.md
```

## Data & Versioning
- Raw data tracked by DVC: `data/raw/insurance.csv.dvc` with remote storage in `dvc_storage/`.
- Pull data: `python -m dvc pull`
- Check status: `python -m dvc status`

## How to Run
```bash
python -m venv venv
.\venv\Scripts\activate         # Windows
pip install -r requirements.txt
python -m dvc pull              # fetch raw data
```
- EDA: open `notebooks/01_eda.ipynb`.
- Hypothesis tests: `notebooks/03_hypothesis_testing.ipynb`.
- ML & pricing: `notebooks/04_ml_modeling.ipynb` or reuse functions in `src/ml_utils.py`.

## Modeling Highlights (Task 4)
- **Targets**: severity (`charges | has_claim=1`), premium proxy (`charges`), claim probability (`has_claim`).
- **Models**: Linear Regression, Decision Tree, Random Forest, XGBoost; Logistic Regression for classification.
- **Metrics**: RMSE/R²/MAE for regression; accuracy/precision/recall/F1 for classification.
- **Interpretability**: SHAP summaries and top features; business notes (e.g., smoker and BMI materially lift predicted severity/premium; age has monotonic effect).
- **Utilities**: `src/ml_utils.py` covers prep (one-hot/label), splits, training, comparison tables, feature importance, SHAP calculators, and risk-based premium illustration.

## Key Findings
- **EDA**: Charges skewed with 10% high-cost outliers; smokers and higher BMI correlate with higher charges; Southeast shows higher mean charges but not statistically significant.
- **Hypothesis Testing**: No significant differences by region (p≈0.19) or gender (p≈0.73); zip-level analysis not possible with current data.
- **ML**: Tree-based models outperform linear baselines on severity/premium; smoking status, BMI, and age dominate importance; risk-based pricing combines claim probability with severity estimates.

## CI/CD
- GitHub Actions workflow runs lint/format/notebook checks on push/PR.

## License
See `LICENSE` for details.