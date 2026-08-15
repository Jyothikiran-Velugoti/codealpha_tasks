import requests
import pandas as pd
from bs4 import BeautifulSoup
def scrape_books():
    url = "https://books.toscrape.com/"

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    book_data = []

    for book in books:
        title = book.h3.a["title"]

        price = (
            book.find("p", class_="price_color")
            .text.replace("£", "")
            .strip()
        )

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = (
            book.find("p", class_="instock availability")
            .text.strip()
        )

        book_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    return pd.DataFrame(book_data)
def save_to_csv(df):
    df.to_csv("data/books.csv", index=False)
    print("CSV file created successfully!")
def main():
    print("Scraping Started...")

    df = scrape_books()

    save_to_csv(df)

    print(f"Successfully scraped {len(df)} books.")
    print("Scraping Completed!")
if __name__ == "__main__":
    main()
   