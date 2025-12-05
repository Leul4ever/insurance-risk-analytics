# Setup Guide

## Initial Setup

### 1. Git Repository Setup

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Project structure and documentation"

# Create and switch to task-1 branch
git checkout -b task-1

# Verify branch
git branch
```

### 2. Python Environment Setup

```bash
# Create virtual environment (if not already created)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
# Check Python version (should be 3.8+)
python --version

# Verify key packages
python -c "import pandas, numpy, matplotlib, seaborn, jupyter; print('All packages installed successfully!')"
```

### 4. Start Jupyter Notebook

```bash
# Start Jupyter Lab
jupyter lab

# Or start classic Jupyter Notebook
jupyter notebook
```

### 5. Project Structure Verification

Ensure your project has the following structure:

```
insurance-risk-analytics/
├── data/
│   ├── raw/              # Original data (move insurance.csv here)
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
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── README.md
├── TASKS.md
├── DELIVERABLES.md
├── SETUP.md
├── .gitignore
└── LICENSE
```

## Next Steps

1. **Move data file**: Move `data/row/insurance.csv` to `data/raw/insurance.csv`
2. **Start EDA**: Open `notebooks/01_eda.ipynb` and begin exploratory analysis
3. **Follow TASKS.md**: Check off tasks as you complete them
4. **Regular commits**: Commit your work at least 3 times per day

## Daily Workflow

```bash
# Start your day
git checkout task-1
git pull  # If working with remote

# Make changes, work on notebooks, etc.

# Commit frequently (at least 3 times per day)
git add .
git commit -m "Descriptive commit message"

# End of day
git push  # If working with remote
```

## Troubleshooting

### Issue: Package installation fails
- Ensure you're using Python 3.8+
- Try upgrading pip: `python -m pip install --upgrade pip`
- Install packages one by one to identify problematic packages

### Issue: Jupyter not starting
- Ensure virtual environment is activated
- Reinstall jupyter: `pip install --upgrade jupyter jupyterlab`

### Issue: Import errors in notebooks
- Ensure kernel is using the correct Python environment
- In Jupyter: Kernel > Change Kernel > Select your venv

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Jupyter Notebook Tips](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

