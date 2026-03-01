# Student Software Pricing Project

This project helps students find the best deals on software by analyzing a dataset of student discounts.

## Files

### 1. `student_pricing_analysis.py`
This is the **Python script** that crunches the numbers to find the best savings.
- **Data Cleaning:** It reads the raw CSV data and converts prices and percentages into numbers for calculation.
- **Analysis:** It performs several checks:
    - Identifies software that is **100% free** for students.
    - Finds the deals with the highest percentage discounts.
    - Calculates the average cost for different categories (e.g., Design, Security).
    - Sums up the total potential monthly savings if a student were to use all these offers.

### 2. `student_software_pricing.csv`
This is the **Dataset** containing information on various software subscriptions.
- **Columns:**
    - `Software_Name`: The name of the product.
    - `Category`: The type of software (e.g., Productivity, Design, Dev).
    - `Standard_Price_Monthly_USD`: The regular price.
    - `Student_Price_Monthly_USD`: The discounted price for students.
    - `Discount_Percentage`: The percent saved.
    - `Verification_Method`: How to prove you are a student (e.g., .edu email, SheerID).
    - `Website_Link`: Where to get the deal.

## Project Goals

The goal of this script is to demonstrate how much money students can save by taking advantage of educational pricing. It highlights:
- **Freebies:** Tools like GitHub Pro, Notion, and Tableau that cost $0 for students.
- **Massive Savings:** How a student could save hundreds of dollars a month compared to standard pricing.

## Data Source (Dataset)

The dataset used in this project was sourced from Kaggle:
[Student Software Discount and Pricing Data](https://www.kaggle.com/datasets/couponswift/student-software-discount-and-pricing-data)