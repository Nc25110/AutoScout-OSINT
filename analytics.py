def analyze_prices(listings):
    avg_price = sum(item["price"] for item in listings) / len(listings)

    for item in listings:
        if item["price"] < avg_price:
            item["status"] = "Below Average"
        else:
            item["status"] = "Above Average"

    return listings
