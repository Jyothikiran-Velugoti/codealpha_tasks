import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    return pd.read_csv("data/books.csv")


def clean_data(df):
    df["Price"] = df["Price"].astype(float)

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["Rating"] = df["Rating"].map(rating_map)

    return df


def analyze_data(df):
    print("Total Books:", len(df))
    print("Average Price:", df["Price"].mean())
    print("Highest Price:", df["Price"].max())
    print("Lowest Price:", df["Price"].min())
    print("Average Rating:", df["Rating"].mean())

    print("\nRating Counts:")
    print(df["Rating"].value_counts())

    top_rated = df[df["Rating"] == 5]

    print("\nTop Rated Books:")
    print(top_rated.head())


def create_charts(df):

    # Rating Chart
    rating_counts = df["Rating"].value_counts().sort_index()

    plt.figure(figsize=(6,4))
    plt.bar(rating_counts.index, rating_counts.values)
    plt.title("Book Ratings Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Books")
    plt.savefig("charts/rating_chart.png")
    plt.close()

    # Price Distribution
    plt.figure(figsize=(6,4))
    plt.hist(df["Price"], bins=5)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.savefig("charts/price_distribution.png")
    plt.close()

    # Top 5 Expensive Books
    top5 = df.nlargest(5, "Price")

    plt.figure(figsize=(10,5))
    plt.bar(top5["Title"], top5["Price"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Top 5 Expensive Books")
    plt.tight_layout()
    plt.savefig("charts/top5_expensive_books.png")
    plt.close()

    # Rating Pie Chart
    plt.figure(figsize=(6,6))
    plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f%%")
    plt.title("Rating Distribution")
    plt.savefig("charts/rating_pie_chart.png")
    plt.close()

    # Price Line Chart
    plt.figure(figsize=(8,5))
    plt.plot(df.index, df["Price"], marker="o")
    plt.title("Price Trend")
    plt.xlabel("Book Index")
    plt.ylabel("Price")
    plt.savefig("charts/price_line_chart.png")
    plt.close()


def main():
    df = load_data()
    df = clean_data(df)

    analyze_data(df)
    create_charts(df)

    print("\nAnalysis Completed Successfully!")


if __name__ == "__main__":
    main()