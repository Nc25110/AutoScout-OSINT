from scraper import get_listings
from analytics import analyze_prices
from exporter import export_csv

def main():
    listings = get_listings()
    analyzed = analyze_prices(listings)
    export_csv(analyzed)

    for item in analyzed:
        print(item)

if __name__ == "__main__":
    main()
