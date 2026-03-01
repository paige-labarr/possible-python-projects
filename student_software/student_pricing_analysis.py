import csv
import os
from collections import Counter

def load_data(filepath):
    """Loads the CSV and converts numbers so we can do math on them!"""
    data = []
    if not os.path.exists(filepath):
        print(f"😱 Oh no! Couldn't find the file at {filepath}")
        return []
    
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Clean up the data: Convert strings to numbers
                try:
                    row['Standard_Price_Monthly_USD'] = float(row['Standard_Price_Monthly_USD'])
                    row['Student_Price_Monthly_USD'] = float(row['Student_Price_Monthly_USD'])
                    # Remove the '%' sign and convert to a number
                    row['Discount_Percentage'] = float(row['Discount_Percentage'].replace('%', ''))
                except ValueError:
                    continue # Skip rows if data is messy
                data.append(row)
    except Exception as e:
        print(f"😭 Error reading file: {e}")
        
    return data

def analyze_deals(data):
    print("\n🎉✨ WELCOME TO THE ULTIMATE STUDENT SAVINGS FINDER! ✨🎉\n")
    
    # 1. Find Free Stuff
    free_stuff = [item for item in data if item['Student_Price_Monthly_USD'] == 0.0]
    print(f"🤑 YAY! We found {len(free_stuff)} items that are COMPLETELY FREE! 💸")
    print("Here are a few highlights:")
    for item in free_stuff[:5]:
        print(f"   🎁 {item['Software_Name']} ({item['Category']}) - Save ${item['Standard_Price_Monthly_USD']:.2f}/mo!")
    print(f"   ...and {len(free_stuff) - 5} more amazing freebies!\n")

    # 2. Best Discounts (non-free but huge savings)
    # Filter out free stuff to show paid deals with high % off
    paid_stuff = [item for item in data if item['Student_Price_Monthly_USD'] > 0.0]
    sorted_discounts = sorted(paid_stuff, key=lambda x: x['Discount_Percentage'], reverse=True)
    
    print("🔥 HOTTEST DEALS (Huge % Off!) 🔥")
    for item in sorted_discounts[:5]:
        print(f"   🚀 {item['Software_Name']}: {item['Discount_Percentage']}% OFF! (Pay only ${item['Student_Price_Monthly_USD']:.2f})")
    print("")

    # 3. Average Price by Category
    categories = {}
    for item in data:
        cat = item['Category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item['Student_Price_Monthly_USD'])
    
    print("📊 AVERAGE STUDENT COST PER CATEGORY 📊")
    for cat, prices in categories.items():
        avg_price = sum(prices) / len(prices)
        if avg_price == 0:
            print(f"   🎈 {cat}: LITERALLY FREE (Average: $0.00)")
        else:
            print(f"   💰 {cat}: ${avg_price:.2f}/mo")

    # 4. Total Savings
    total_standard = sum(item['Standard_Price_Monthly_USD'] for item in data)
    total_student = sum(item['Student_Price_Monthly_USD'] for item in data)
    total_savings = total_standard - total_student
    
    print("\n💰💰💰 THE GRAND TOTAL 💰💰💰")
    print(f"If you bought ALL this software at regular price: ${total_standard:.2f} per month")
    print(f"Student Price for EVERYTHING: ${total_student:.2f} per month")
    print(f"🤯 TOTAL MONTHLY SAVINGS: ${total_savings:.2f}!!! THAT IS ABSOLUTELY BONKERS! 🤯")
    
    # 5. Verification Methods
    methods = [item['Verification_Method'] for item in data]
    common_methods = Counter(methods).most_common(3)
    print("\n🔐 HOW TO GET THESE DEALS (Top Methods) 🔐")
    for method, count in common_methods:
        print(f"   🔑 {method}: {count} deals")

if __name__ == "__main__":
    # Find the CSV file in the same folder as this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "student_software_pricing.csv")
    
    data = load_data(csv_path)
    if data:
        analyze_deals(data)