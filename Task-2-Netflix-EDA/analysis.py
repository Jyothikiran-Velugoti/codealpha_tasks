import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Data/netflix_titles.csv")

print("=" * 50)
print("NETFLIX DATASET OVERVIEW")
print("=" * 50)

# First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumns:")
print(df.columns)

# Dataset Information
print("\nDataset Info:")
df.info()

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe(include="all"))
print("\n" + "=" * 50)
print("DATA CLEANING")
print("=" * 50)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)
print("\n" + "=" * 50)
print("MOVIES VS TV SHOWS")
print("=" * 50)

# Count Movies and TV Shows
content_count = df["type"].value_counts()

print(content_count)

# Create Bar Chart
plt.figure(figsize=(6,4))
content_count.plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("Charts/movies_vs_tvshows.png")

plt.show()
print("\n" + "=" * 50)
print("TOP 10 COUNTRIES")
print("=" * 50)

# Top 10 Countries
top_countries = df["country"].dropna().value_counts().head(10)

print(top_countries)

# Bar Chart
plt.figure(figsize=(10,6))
top_countries.plot(kind="bar")

plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Charts/top10_countries.png")

plt.show()
print("\n" + "=" * 50)
print("CONTENT ADDED BY YEAR")
print("=" * 50)

# Remove missing values
year_data = df.dropna(subset=["release_year"])

# Count content by release year
year_count = year_data["release_year"].value_counts().sort_index()

print(year_count)

# Line Chart
plt.figure(figsize=(12,6))
plt.plot(year_count.index, year_count.values, marker="o")

plt.title("Netflix Content Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)

plt.tight_layout()

plt.savefig("Charts/content_by_year.png")

plt.show()
print("\n" + "=" * 50)
print("CONTENT RATINGS ANALYSIS")
print("=" * 50)

# Count Ratings
rating_count = df["rating"].dropna().value_counts()

print(rating_count)

# Bar Chart
plt.figure(figsize=(10,6))
rating_count.plot(kind="bar")

plt.title("Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Charts/content_ratings.png")

plt.show()
print("\n" + "=" * 50)
print("BUSINESS INSIGHTS")
print("=" * 50)

print("1. Movies are available in greater numbers than TV Shows.")
print("2. The United States has the highest Netflix content.")
print("3. Netflix content increased significantly after 2015.")
print("4. TV-MA is one of the most common content ratings.")
print("5. Netflix focuses heavily on movie content and global expansion.")
