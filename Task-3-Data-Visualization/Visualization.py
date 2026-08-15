# Import Required Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Load Dataset Function

def load_data():
    try:
        df = pd.read_csv("Data/netflix_titles.csv")
        print("Dataset loaded successfully!")
        return df

    except FileNotFoundError:
        print("Dataset file not found!")
        return None


# Data Cleaning Function

def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df["director"] = df["director"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Not Rated")

    # Convert date column into datetime format
    df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

    print("Data cleaning completed!")

    return df
# Chart 1: Movies vs TV Shows

def movies_vs_tvshows(df):

    plt.figure(figsize=(8,5))

    sns.countplot(
        data=df,
        x="type"
    )

    plt.title("Movies vs TV Shows Distribution")
    plt.xlabel("Content Type")
    plt.ylabel("Number of Titles")

    plt.tight_layout()

    plt.savefig(
        "Charts/01_movies_vs_tvshows.png",
        dpi=300
    )

    plt.close()

    print("Chart 1 created successfully!")
# Chart 2: Content Added By Year

def content_added_by_year(df):

    yearly_content = df["date_added"].dt.year.value_counts().sort_index()

    plt.figure(figsize=(10,5))

    sns.lineplot(
        x=yearly_content.index,
        y=yearly_content.values,
        marker="o"
    )

    plt.title("Netflix Content Added By Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "Charts/02_content_added_by_year.png",
        dpi=300
    )

    plt.close()

    print("Chart 2 created successfully!")
    # Chart 3: Top 10 Countries

def top10_countries(df):

    countries = (
        df["country"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,5))

    sns.barplot(
        x=countries.values,
        y=countries.index
    )

    plt.title("Top 10 Countries Producing Netflix Content")
    plt.xlabel("Number of Titles")
    plt.ylabel("Country")

    plt.tight_layout()

    plt.savefig(
        "Charts/03_top10_countries.png",
        dpi=300
    )

    plt.close()

    print("Chart 3 created successfully!")
# Chart 4: Top 10 Genres

def top10_genres(df):

    genres = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,5))

    sns.barplot(
        x=genres.values,
        y=genres.index
    )

    plt.title("Top 10 Netflix Genres")
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")

    plt.tight_layout()

    plt.savefig(
        "Charts/04_top10_genres.png",
        dpi=300
    )

    plt.close()

    print("Chart 4 created successfully!")
# Chart 5: Rating Distribution

def rating_distribution(df):

    ratings = df["rating"].value_counts().head(10)

    plt.figure(figsize=(10,5))

    sns.barplot(
        x=ratings.values,
        y=ratings.index
    )

    plt.title("Netflix Rating Distribution")
    plt.xlabel("Number of Titles")
    plt.ylabel("Rating")

    plt.tight_layout()

    plt.savefig(
        "Charts/05_rating_distribution.png",
        dpi=300
    )

    plt.close()

    print("Chart 5 created successfully!")
# Chart 6: Top 10 Directors

def top10_directors(df):

    directors = (
        df["director"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,5))

    sns.barplot(
        x=directors.values,
        y=directors.index
    )

    plt.title("Top 10 Directors on Netflix")
    plt.xlabel("Number of Titles")
    plt.ylabel("Director")

    plt.tight_layout()

    plt.savefig(
        "Charts/06_top10_directors.png",
        dpi=300
    )

    plt.close()

    print("Chart 6 created successfully!")
# Chart 7: Movie Duration Distribution

def movie_duration_distribution(df):

    movies = df[df["type"] == "Movie"].copy()

    movies["duration"] = (
        movies["duration"]
        .str.replace(" min", "")
        .astype(float)
    )

    plt.figure(figsize=(10,5))

    sns.histplot(
        data=movies,
        x="duration",
        bins=30
    )

    plt.title("Movie Duration Distribution")
    plt.xlabel("Duration (Minutes)")
    plt.ylabel("Number of Movies")

    plt.tight_layout()

    plt.savefig(
        "Charts/07_movie_duration_distribution.png",
        dpi=300
    )

    plt.close()

    print("Chart 7 created successfully!")
# Chart 8: Release Year Trend

def release_year_trend(df):

    release_year = (
        df["release_year"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(10,5))

    sns.lineplot(
        x=release_year.index,
        y=release_year.values
    )

    plt.title("Netflix Content Release Year Trend")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "Charts/08_release_year_trend.png",
        dpi=300
    )

    plt.close()

    print("Chart 8 created successfully!")
# Main Execution

if __name__ == "__main__":

    df = load_data()

    if df is not None:

        df = clean_data(df)

        movies_vs_tvshows(df)

        content_added_by_year(df)

        top10_countries(df)
        top10_genres(df)
        rating_distribution(df)
        top10_directors(df)
        movie_duration_distribution(df)
        release_year_trend(df)
    

