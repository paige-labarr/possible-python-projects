# Streaming Service Analysis Project

This project analyzes content catalogs from major streaming platforms (Netflix, Hulu, Amazon Prime) to provide insights into their libraries.

## Files

### 1. `streaming.py`
This is the main **Python script** that performs the data analysis.
- **User Input:** It prompts the user to select a platform (`netflix`, `hulu`, or `prime`).
- **Analysis:** Based on the selection, it loads the corresponding dataset and calculates:
    - The ratio of Movies vs. TV Shows.
    - The top 5 most common genres.
    - The top 5 countries producing content.
    - The most frequent content rating (e.g., TV-MA, PG-13).

### 2. Data Files (`*.csv`)
These CSV (Comma Separated Values) files contain the raw catalog data for each service.
- `netflix_titles.csv`: Data for Netflix.
- `hulu_titles.csv`: Data for Hulu.
- `amazon_prime_titles.csv`: Data for Amazon Prime Video.

Each file typically contains columns for `type` (Movie/TV Show), `title`, `director`, `cast`, `country`, `release_year`, `rating`, `duration`, and `listed_in` (genres).

## Data Sources (Datasets)

The datasets used in this project were sourced from Kaggle:
- [Amazon Prime](https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows)
- [Hulu](https://www.kaggle.com/datasets/shivamb/hulu-movies-and-tv-shows)
- [Netflix](https://www.kaggle.com/datasets/shivamb/netflix-shows)