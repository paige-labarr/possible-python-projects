import csv
import os

def load_data(filepath):
    """Loads Titanic data from CSV and converts numbers to proper formats."""
    data = []
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return []
    
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # We need to convert strings to numbers to do math
                try:
                    # Survived is 0 or 1
                    row['Survived'] = int(row['Survived'])
                    # Pclass is 1, 2, or 3
                    row['Pclass'] = int(row['Pclass'])
                    
                    # Age might be empty (missing data)
                    if row['Age']:
                        row['Age'] = float(row['Age'])
                    else:
                        row['Age'] = None
                        
                    # SibSp (Siblings/Spouses) and Parch (Parents/Children)
                    row['SibSp'] = int(row['SibSp'])
                    row['Parch'] = int(row['Parch'])
                    
                    # Fare might be missing or 0
                    if row['Fare']:
                        row['Fare'] = float(row['Fare'])
                    else:
                        row['Fare'] = 0.0
                        
                    data.append(row)
                except ValueError:
                    continue # Skip rows with bad data
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return data

def get_survival_rate(data_subset):
    """Calculates the percentage of survivors in a list of passengers."""
    if not data_subset:
        return 0.0
    survivors = sum(1 for p in data_subset if p['Survived'] == 1)
    return (survivors / len(data_subset)) * 100

def analyze_titanic(data):
    print(f"\n🚢 --- TITANIC DATA ANALYSIS ({len(data)} passengers) --- 🚢\n")
    
    # 1. Survival Analysis: Women and Children First?
    print("1. Survival Rates by Group:")
    
    # Filter lists for different groups
    # Note: We treat 'Child' as under 18
    children = [p for p in data if p['Age'] is not None and p['Age'] < 18]
    adult_women = [p for p in data if p['Sex'] == 'female' and (p['Age'] is None or p['Age'] >= 18)]
    adult_men = [p for p in data if p['Sex'] == 'male' and (p['Age'] is None or p['Age'] >= 18)]
    
    print(f"   - Children (<18): {get_survival_rate(children):.1f}% survival rate")
    print(f"   - Adult Women:    {get_survival_rate(adult_women):.1f}% survival rate")
    print(f"   - Adult Men:      {get_survival_rate(adult_men):.1f}% survival rate")
    
    # 2. Class Privilege
    print("\n2. Survival Rates by Class:")
    for pclass in [1, 2, 3]:
        class_passengers = [p for p in data if p['Pclass'] == pclass]
        rate = get_survival_rate(class_passengers)
        print(f"   - Class {pclass}: {rate:.1f}%")
        
    # 3. Demographics
    print("\n3. Demographics:")
    # Filter out missing ages for average calculation
    valid_ages = [p['Age'] for p in data if p['Age'] is not None]
    avg_age = sum(valid_ages) / len(valid_ages) if valid_ages else 0
    print(f"   - Average Age: {avg_age:.1f} years old")
    
    # Count genders
    males = len([p for p in data if p['Sex'] == 'male'])
    females = len([p for p in data if p['Sex'] == 'female'])
    print(f"   - Gender Split: {males} Males vs {females} Females")
    
    # 4. Economics (Fares)
    print("\n4. Ticket Prices (Economics):")
    fares = [p['Fare'] for p in data]
    print(f"   - Most Expensive Ticket: ${max(fares):.2f}")
    print(f"   - Average Ticket Price:  ${sum(fares) / len(fares):.2f}")
    
    # Compare fares of survivors vs non-survivors
    survivor_fares = [p['Fare'] for p in data if p['Survived'] == 1]
    victim_fares = [p['Fare'] for p in data if p['Survived'] == 0]
    
    avg_surv_fare = sum(survivor_fares) / len(survivor_fares) if survivor_fares else 0
    avg_victim_fare = sum(victim_fares) / len(victim_fares) if victim_fares else 0
    
    print(f"   - Avg Fare (Survivors):      ${avg_surv_fare:.2f}")
    print(f"   - Avg Fare (Non-Survivors):  ${avg_victim_fare:.2f}")
    
    # 5. Family Size
    print("\n5. Family & Group Travel:")
    # Family Size = SibSp (Siblings/Spouse) + Parch (Parents/Children)
    solo_travelers = [p for p in data if (p['SibSp'] + p['Parch']) == 0]
    family_travelers = [p for p in data if (p['SibSp'] + p['Parch']) > 0]
    
    print(f"   - Solo Travelers Survival:   {get_survival_rate(solo_travelers):.1f}%")
    print(f"   - Family Travelers Survival: {get_survival_rate(family_travelers):.1f}%")

if __name__ == "__main__":
    # Setup path to the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "titanic_data.csv")
    
    titanic_data = load_data(csv_path)
    
    if titanic_data:
        analyze_titanic(titanic_data)