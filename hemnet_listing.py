import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def clean_price_string(price_string):
    # Remove non-breaking spaces
    cleaned_string = price_string.replace('\xa0', ' ')
    # Remove leading and trailing whitespaces
    cleaned_string = cleaned_string.strip()
    return cleaned_string

def wrap_image(image_url):
    return '=IMAGE("' + image_url + '")'

def extract_property_info(url):
    # Set up the headless browser
    options = Options()
    options.add_argument("--headless")  # Run the browser in headless mode
    service = Service('/path/to/chromedriver')  # Replace with the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=options)

    # Load the website and solve the JavaScript challenge
    driver.get(url)

    # Implement the necessary steps to solve the JavaScript challenge
    # This may involve filling out forms, clicking buttons, or executing JavaScript code

    # Wait for the challenge to be solved and retrieve the HTML content
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")
    property_info = {}

    # Property image URL
    property_image_element = soup.find('div', class_='property-carousel js-carousel-container qa-carousel')
    if property_image_element:
        image_element = property_image_element.find('img', class_='property-gallery__item')
        image_url = image_element['src'] if image_element else ''
        property_info['Property image URL'] = wrap_image(image_url)

    # Extract the desired information using BeautifulSoup with error handling
    address_element = soup.find('h1', class_='qa-property-heading')
    property_info['address'] = address_element.text.strip() if address_element else ""

    # Price
    listed_price_element = soup.find('p', class_='qa-property-price')
    property_info['price'] = clean_price_string(listed_price_element.text.strip() if listed_price_element else "")

    # Size
    size_element = soup.find('dt', text='Antal rum')
    property_info['Size'] = size_element.find_next('dd').text.strip() if size_element else ''
    # Area
    area_element = soup.find('dt', text='Boarea')
    property_info['Area'] = area_element.find_next('dd').text.strip() if area_element else ''

    # Floor
    floor_element = soup.find('dt', text='Våning')
    property_info['Floor'] = floor_element.find_next('dd').text.strip() if floor_element else ''

    # Year of Construction
    construction_element = soup.find('dt', text='Byggår')
    property_info['Year of Construction'] = construction_element.find_next('dd').text.strip() if construction_element else ''

    # Association/BRF Name
    association_element = soup.find('dt', text='Förening')
    association_name_element = association_element.find_next('span', class_='property-attributes-table__value')
    property_info['Association Name'] = association_name_element.text.strip() if association_name_element else ''

    # Avgift
    avgift_element = soup.find('dt', text='Avgift')
    property_info['avgift'] = clean_price_string(avgift_element.find_next('dd').text.strip()) if avgift_element else ''

    # Pris/m²
    prism2_element = soup.find('dt', text='Pris/m²')
    property_info['Pris/m²'] = clean_price_string(prism2_element.find_next('dd').text.strip()) if prism2_element else ''

    # Broker name
    broker_name_element = soup.find('p', class_='broker-card__text qa-broker-name')

    property_info['Broker name'] = broker_name_element.text.strip() if broker_name_element else ''
    property_info['Broker link'] = broker_name_element.find('a')['href'].strip() if broker_name_element else ''

    # Broker name and image
    broker_card_element = soup.find('div', class_='broker-card__avatar')
    if broker_card_element:
        broker_image_element = broker_card_element.find('img', class_='broker-card__image')
        broker_image_url = broker_image_element['data-src'] if broker_image_element else ''
        property_info['Broker image'] = wrap_image(broker_image_url.strip())

    # viewing times
    # Find the viewing times list element
    viewing_times_list = soup.find('ul', class_='listing-showings__list qa-showings-list')

    # Find all viewing time items
    viewing_time_items = viewing_times_list.find_all('li', class_='listing-showings__showing') if viewing_times_list else None

    # Extract the viewing times
    viewing_times = []
    if not viewing_time_items:
        property_info['viewing times'] = ""
    else:
        for item in viewing_time_items:
            time_element = item.find('span', class_='listing-showings__showing-time')
            if time_element:
                viewing_times.append(time_element.text.strip())
        property_info['viewing times'] = viewing_times

    # BRF rating
    ratings_element = soup.find('div', class_='housing-cooperative')

    # Extract the highest applicable rating
    highest_rating = ''
    if ratings_element:
        rating_spans = ratings_element.find_all('span', class_='housing-cooperative__rating--high')
        if rating_spans:
            highest_rating = rating_spans[0].text.strip()

    property_info['BRF rating'] = highest_rating

    return property_info

# Read URLs from standard input (piped from hemnet.py)
for url in sys.stdin:
    url = url.strip()  # Remove leading/trailing whitespaces and newline characters

    
    output = extract_property_info(url)
    
    #output = {}

    # Define the order of column names in the TSV
    column_names = [
        'Property image URL', 'address','viewing times', 'price', 'Size', 'Area', 'Floor', 'Year of Construction',
        'Association Name', 'avgift', 'Pris/m²', 'Broker name', 'Broker image',  'BRF rating'
    ]

    # Output the property information in TSV format
    tsv_output = ''
    for column in column_names:
        tsv_output += str(output.get(column, '')) + '\t'
    tsv_output = tsv_output.strip()

    print(tsv_output)
