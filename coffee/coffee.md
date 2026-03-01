# Coffee Menu Analysis Project

This project consists of two main files that work together to analyze a coffee shop's menu.

## Files

### 1. `coffee_menu.csv`
This is a **Comma Separated Values** file that acts as a simple database. It stores the raw menu data.
- **Columns:** `Name`, `Size`, `Price`
- **Purpose:** To hold the persistent data about drink options and pricing.

### 2. `coffee_project.py`
This is the **Python script** that contains the logic for the application.
- **Functions:**
    - `load_menu(filepath)`: Opens the CSV file and converts prices into numbers.
    - `print_menu(menu)`: Displays the full list of items to the user.
    - `analyze_menu(menu)`: Calculates statistics like the most expensive item, cheapest drink, and average prices by size.

## How They Work Together

1. **Loading Data:** When you run `coffee_project.py`, it looks for `coffee_menu.csv` in the same folder.
2. **Parsing:** The Python script reads the CSV file line by line using the `csv` library.
3. **Processing:** The script converts the text prices (like "3.00") into decimal numbers (floats) so it can perform calculations.
4. **Reporting:** Finally, the script prints the full menu and then generates an analysis report, highlighting key pricing insights and available add-ons.