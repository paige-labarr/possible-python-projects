import csv
import os

def load_menu(filepath):
    """Reads the menu CSV and converts prices to numbers."""
    menu = []
    
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        return []
    
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Convert Price to a float (decimal number) so we can do math
                    row['Price'] = float(row['Price'])
                    menu.append(row)
                except ValueError:
                    continue # Skip rows with bad data
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return menu

def print_menu(menu):
    print("\n📋 --- FULL MENU ---")
    for item in menu:
        print(f"   • {item['Name']} ({item['Size']}): ${item['Price']:.2f}")

def analyze_menu(menu):
    print(f"\n☕ --- COFFEE MENU ANALYSIS ({len(menu)} items) --- ☕\n")
    
    # Separate drinks from add-ons based on Size
    # In the CSV, add-ons have Size = "Add"
    drinks = [item for item in menu if item['Size'] != 'Add']
    addons = [item for item in menu if item['Size'] == 'Add']
    
    # 1. Most Expensive Item (Overall)
    # We use max() with a key to find the item with the highest price
    most_expensive = max(menu, key=lambda x: x['Price'])
    print(f"1. Most Expensive Item:\n   💎 {most_expensive['Name']} ({most_expensive['Size']}) - ${most_expensive['Price']:.2f}")
    
    # 2. Cheapest Drink (excluding add-ons)
    if drinks:
        cheapest_drink = min(drinks, key=lambda x: x['Price'])
        print(f"\n2. Cheapest Drink:\n   🏷️  {cheapest_drink['Name']} ({cheapest_drink['Size']}) - ${cheapest_drink['Price']:.2f}")
        
    # 3. Average Prices (Small vs Large)
    small_prices = [d['Price'] for d in drinks if d['Size'] == 'Small']
    large_prices = [d['Price'] for d in drinks if d['Size'] == 'Large']
    
    avg_small = sum(small_prices) / len(small_prices) if small_prices else 0
    avg_large = sum(large_prices) / len(large_prices) if large_prices else 0
    
    print("\n3. Average Drink Prices:")
    print(f"   - Small: ${avg_small:.2f}")
    print(f"   - Large: ${avg_large:.2f}")
    
    # 4. Add-ons
    print(f"\n4. Add-ons ({len(addons)} available):")
    for item in addons:
        print(f"   + {item['Name']} (+${item['Price']:.2f})")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Note: We are now using the MENU csv, not the inventory one!
    csv_path = os.path.join(current_dir, 'coffee_menu.csv')
    
    menu_data = load_menu(csv_path)
    
    if menu_data:
        print_menu(menu_data)
        analyze_menu(menu_data)