import csv
import os

#author's note - mEdium and largE have a capital E on purpose for Espresso added
#these "E" drinks have a higher price (due to espresso) and separate cups (added sticker) from their non-espresso counterparts!
#a mEdium or largE after 10 am may cause insomnia - not recommended

def read_coffee_inventory(filepath):
    """
    reads coffee inventory data from a csv file and returns it as a list of dictionaries
    a dictionary stores key-value pairs - the key is the column header and value is the corresponding value in that row
    DictReader maps the column headers to the values in each row so you can access data by column name
    """
    inventory_data = []
    
    # check if the file exists
    if not os.path.exists(filepath):
        print(f"the csv file was not found here: {filepath}")
        print("check your directory by using 'pwd' in the terminal")
        print("change the directory if needed using 'cd' then the location")
        print("or relocate the csv file so it's in the working directory")
        return inventory_data

    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file: #r for read mode
            # csv.DictReader reads the first line as the keys for the dictionaries
            reader = csv.DictReader(file)
            
            print(f"SUCCESS - opened & reading data from: {filepath}\n")
            
            for row in reader:
                try:
                    # create a dictionary
                    item = {
                        'Size': row['Size'],
                        'Price': float(row['Price']), #convert price to float (data from csv is read as string)
                        'Inventory': int(row['Inventory']) #convert inventory to int (same reason as above)
                    }
                    inventory_data.append(item)
                except ValueError as e:
                    print(f"row skipped - data conversion error in row {row}: {e}")
                    continue

        return inventory_data

    except IOError as e:
        print(f"error reading file {filepath}: {e}")
        return inventory_data


if __name__ == "__main__":
    # the CSV file must be in the same directory (folder) as this Python script
    # if elsewhere, relocate or specify the correct file path
    csv_filename = 'coffee_inventory.csv'
    
    # read the data from the csv & store as inventory
    inventory = read_coffee_inventory(csv_filename)
    
    if inventory:
        print("- - - - Paige's Place ☕ ☕ INVENTORY - - - -")
        
        # total number of cups in stock
        total_cups = sum(item['Inventory'] for item in inventory)
        
        # formatted report
        for item in inventory:
            # .2f to round to two decimal places for the price
            # <6 will left aligns the size (of the coffee) and ensure it takes up at least 6 characters for consistent formatting
            # string alignment source: https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/
            print(f"   ☕ {item['Size']:<6} | ${item['Price']:.2f} | Cups Remaining: {item['Inventory']}")
            
        print(f"   Total supply of remaining cups ---> {total_cups}")
        print("- " * 23)
    else:
        print("OH NO - inventory is empty or couldn't be loaded")