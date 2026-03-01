# Titanic Data Analysis Project

This project analyzes the famous Titanic passenger manifest to explore factors that influenced survival rates.

## Files

### 1. `titanic_project.py`
This is the **Python script** that performs the data analysis.
- **Data Cleaning:** It loads the raw CSV data and converts strings (like "male"/"female" or numbers in text format) into usable data types.
- **Analysis:** It calculates statistics to answer key questions:
    - **"Women and Children First":** Did these groups actually have higher survival rates?
    - **Class Privilege:** How did being in 1st, 2nd, or 3rd class affect survival chances?
    - **Economics:** What was the average fare, and did paying more help you survive?
    - **Demographics:** Breakdowns of age, gender, and family size.

### 2. `titanic_data.csv`
This is the **Dataset** containing the passenger list.
- **Columns:**
    - `Survived`: 0 = No, 1 = Yes.
    - `Pclass`: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
    - `Name`, `Sex`, `Age`: Basic demographic info.
    - `SibSp`: # of siblings / spouses aboard.
    - `Parch`: # of parents / children aboard.
    - `Fare`: Passenger fare.
    - `Embarked`: Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

## Data Source (Dataset)

The dataset used in this project was sourced from Kaggle:
[Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)