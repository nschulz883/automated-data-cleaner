#  Automated Data Cleaning Tool

##  Overview

This project is a Python-based automated data cleaning pipeline that processes raw CSV files and prepares them for analysis or machine learning tasks.

It handles missing values, feature engineering, encoding, scaling, and generates reports and visualisations.

##  Objective

To automate the preprocessing of datasets by:

* Cleaning missing and duplicate data
* Transforming features
* Encoding categorical variables
* Scaling numerical features
* Generating reports and visual insights

##  Features

* Removes duplicate rows
* Fills missing values:

  * Numerical → mean
  * Categorical → mode
* Feature engineering:

  * Squared features
  * Log transformations
* One-hot encoding
* Min-Max scaling
* Generates:

  * Cleaned dataset
  * Summary report
  * Distribution plots

##  Example Workflow

1. Input a CSV file
2. Script processes the data
3. Outputs:

   * cleaned_data.csv
   * report.txt
   * distribution plots

##  Project Structure

```bash
automated-data-cleaning-tool/
│── README.md
│── requirements.txt
│── src/
│   └── main.py
│── outputs/
```

##  How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

Then enter your CSV file path when prompted.

##  Output Files

* `cleaned_data.csv` → processed dataset
* `report.txt` → summary of dataset
* `*.png` → distribution plots

##  Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

##  Future Improvements

* Add outlier detection
* Add data quality scoring
* Build a web interface
* Support large datasets


