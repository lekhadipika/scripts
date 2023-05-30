import csv
import requests
from bs4 import BeautifulSoup


def scrape_link(url):
    # Send a GET request to the URL
    response = requests.get(url)
    data = [""] * 4
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the desired information from the page
        about = soup.find_all("div", class_="_36W0F _2a2Ik")
        for item in about:
            apt_attribute = item.find("div", class_="_2soQI")
            
            if apt_attribute: 
                apt_attr_text = apt_attribute.text.strip()
                if apt_attr_text == "Våning":
                    floor = item.find("div", class_="_18w8g").text.strip()
                    data[0] = floor
                elif apt_attr_text == "Byggår":
                    data[1] =item.find("div", class_="_18w8g").text.strip()
        broker = soup.find("div", class_="_1XCe7")
        broker_link = broker.find("a", class_="n1zfB _1uxTS _3TSQW")
        if broker_link:
            data[2] = broker_link.text.strip()
            # Optional broken link. Uncomment this line if you want broker profile link
            # data[3] = broker_link.get("href")

        return data
    else:
        print("Failed to retrieve the page:", response.status_code)
        return []


# URL of the search results page
num_pages = 3

data = []
for i in range(1, num_pages+1):
    url = "https://www.booli.se/huvudsta/39?objectType=L%C3%A4genhet&hasBalcony=1&minLivingArea=60&maxListPrice=5000000&page={}".format(i)
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing the search results
    results = soup.find_all("a", class_="_2CbdZ")
    print("Len results {}".format(len(results)))
    # Prepare the data to be written to the CSV file

    for result in results:
        url = "https://www.booli.se{}".format(result.get("href"))
        title = result.find("h3", class_="SLlk3").text.strip()
        address = result.find("p", class_="_3aHTt").text.strip()
        price_div = result.find("p", class_="_1aPVJ")
        if not price_div:
            price = "Price missing"
        else:
            price = price_div.text.strip()

        # Find elements of class _1zQP5
        features = result.find("div", class_="_1zQP5")
        

        feature_values = [feature.text.strip() for feature in features]
        feature_values = feature_values + [''] * (3 - len(feature_values))
        feature_values.extend(scrape_link(url))
        data.append([title, url, address, price] + feature_values)


# Specify the path and filename for the CSV file
csv_file = "search_results.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    headers = ["Title", "Link", "Address", "Price", "Num rooms", "Area", "Avgift", "Floor", "Year built", "Broker", "Broker Link"]
    writer.writerow(headers)  # Write header row
    writer.writerows(data)  # Write search results

print("Search results have been scraped and saved to", csv_file)
