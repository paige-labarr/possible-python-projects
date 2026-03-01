# Coffee Inventory Project

This project consists of two main files that work together to manage and display coffee inventory data.

## Files

### 1. `coffee_inventory.csv`
This is a **Comma Separated Values** file that acts as a simple database. It stores the raw data in a text format.
- **Columns:** `Size`, `Price`, `Inventory`
- **Purpose:** To hold the persistent data about coffee stock levels and pricing.

### 2. `coffee_project.py`
This is the **Python script** that contains the logic for the application.
- **Functions:**
    - `read_coffee_inventory(filepath)`: Opens the CSV file and converts each row into a Python dictionary.
    - `main` block: Calculates total cups, total value, checks for low stock, and prints a formatted report to the terminal.

## How They Work Together

1. **Loading Data:** When you run `coffee_project.py`, it looks for `coffee_inventory.csv` in the same folder.
2. **Parsing:** The Python script reads the CSV file line by line. It uses the `csv` library to understand the structure (headers vs. data).
3. **Processing:** The script converts the text data (like "2.50" or "53") into numbers (floats and integers) so it can do math.
4. **Reporting:** Finally, the script uses this processed data to generate a user-friendly report, calculating totals and flagging items that need restocking.