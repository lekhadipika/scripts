import sys
import cfscrape
from bs4 import BeautifulSoup

def extract_apartments(url):
    scraper = cfscrape.create_scraper()
    response = scraper.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    apartments = []
    listings = soup.find_all('li', class_='normal-results__hit js-normal-list-item')

    for listing in listings:
        apartment = {}

        # Extract location
        address_element = listing.find('h2', class_='listing-card__street-address')
        if address_element:
            apartment['Location'] = address_element.text.strip()

        # Extract price
        price_element = listing.find('div', class_='listing-card__attribute--primary')
        if price_element:
            apartment['Price'] = price_element.text.strip()

        # Extract number of rooms
        rooms_element = listing.find('div', class_='listing-card__attributes-row').find_all('div', class_='listing-card__attribute--primary')[2]
        if rooms_element:
            apartment['Rooms'] = rooms_element.text.strip()

        # Extract apartment size
        size_element = listing.find('div', class_='listing-card__attributes-row').find_all('div', class_='listing-card__attribute--primary')[1]
        if size_element:
            apartment['Size'] = size_element.text.strip()

        # Extract avgift
        avgift_element = listing.find('div', class_='listing-card__attribute--fee')
        print(avgift_element)
        if avgift_element:
            apartment['Avgift'] = avgift_element.text.strip()

        # Extract viewing time
        showing_element = listing.find('span', class_='listing-card__showing-date')
        if showing_element:
            apartment['Viewing Time'] = showing_element.text.strip()

        # Extract link
        link_element = listing.find('a', class_='js-listing-card-link')
        if link_element:
            apartment['Link'] = link_element['href']

        apartments.append(apartment)

    return apartments

# Check if URL is provided as a command line argument
if len(sys.argv) < 2:
    print('Please provide the webpage URL as a command line argument.')
    sys.exit(1)

url = sys.argv[1]
apartments = extract_apartments(url)

# Print the output with column titles
titles = ['Location', 'Price', 'Rooms', 'Size', 'Avgift', 'Viewing Time', 'Link']
output = '\t'.join(titles) + '\n'
for apartment in apartments:
    output += '\t'.join(apartment.get(title, '') for title in titles) + '\n'

# Print the output
print(output)

