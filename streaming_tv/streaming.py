import csv
import os
from collections import Counter # A helpful tool to count things easily

def get_file_path(platform):
    """Returns the filename based on the user's choice."""
    if platform == "netflix":
        return "netflix_titles.csv"
    elif platform == "hulu":
        return "hulu_titles.csv"
    elif platform == "prime":
        return "amazon_prime_titles.csv"
    else:
        return None

def load_data(filepath):
    """Reads the CSV file and returns a list of dictionaries."""
    data = []
    
    # Check if file exists before trying to open it
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        print("Make sure the CSV file is in the same folder as this script.")
        return []
    
    try:
        # Open the file in read mode ('r') with utf-8 encoding to handle special characters
        with open(filepath, mode='r', encoding='utf-8') as file:
            # DictReader treats the first row as headers and lets us access data by column name
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return data

def analyze_data(data):
    """Performs analysis on the dataset to answer key questions."""
    total_titles = len(data)
    print(f"\n--- Analysis Results ({total_titles} titles found) ---")
    
    # 1. Count Movies vs TV Shows
    # We create a list of just the 'type' column from every row
    types = [row['type'] for row in data]
    # Counter automatically counts how many times each item appears
    type_counts = Counter(types)
    
    print("\n1. Content Type Breakdown:")
    for content_type, count in type_counts.items():
        print(f"   - {content_type}: {count}")
        
    # 2. Top Genres
    # Genres in the CSV are often lists like "Comedy, Drama, Action"
    all_genres = []
    for row in data:
        # We split the string by comma to get individual genres
        genres = row['listed_in'].split(', ')
        all_genres.extend(genres)
    
    # .most_common(5) gives us the top 5 items
    genre_counts = Counter(all_genres).most_common(5)
    print("\n2. Top 5 Genres:")
    for genre, count in genre_counts:
        print(f"   - {genre}: {count}")
        
    # 3. Top Countries
    # We filter out rows where the country is blank
    countries = [row['country'] for row in data if row['country']]
    country_counts = Counter(countries).most_common(5)
    
    print("\n3. Top 5 Countries producing content:")
    for country, count in country_counts:
        print(f"   - {country}: {count}")
        
    # 4. Ratings
    ratings = [row['rating'] for row in data if row['rating']]
    top_rating = Counter(ratings).most_common(1)
    
    if top_rating:
        print(f"\n4. Most Common Rating: {top_rating[0][0]} ({top_rating[0][1]} titles)")

def main():
    print("Streaming Service Data Analyzer")
    print("-------------------------------")
    print("Which platform would you like to analyze?")
    print("Options: Netflix, Hulu, Prime")
    
    # Get user input, convert to lowercase, and remove extra spaces
    choice = input("Enter your choice: ").lower().strip()
    
    filename = get_file_path(choice)
    
    if filename:
        # Construct the full path to the file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, filename)
        
        print(f"\nLoading data from {filename}...")
        data = load_data(full_path)
        
        if data:
            analyze_data(data)
    else:
        print("Invalid selection. Please restart and choose netflix, hulu, or prime.")

if __name__ == "__main__":
    main()