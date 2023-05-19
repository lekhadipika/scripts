# Hemnet Data Extractor
This script extracts apartment information from a given webpage URL and displays the results in a tabular format.

## Prerequisites
- Python 3.6 or higher
- pip package manager

## Installation
Clone the repository or download the script file.

Open a terminal or command prompt and navigate to the directory where the script is located.

Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage
Run the script with the webpage URL as a command line argument. For example:

```
python script_name.py [hemnet_webpage_URL]
```

Replace script_name.py with the actual name of your script file and [hemnet_webpage_URL] with the URL of the webpage you want to extract apartment information from. e.g. https://www.hemnet.se/bostader\?location_ids%5B%5D\=473498\&item_types%5B%5D\=bostadsratt\&rooms_min\=2\&living_area_min\=60\&price_max\=6000000\&open_house_phrase\=weekend

The script will fetch the apartment data from the provided URL and display it in a tabular format.


## Output
The script will output the apartment information in a tabular format, including details such as location, price, number of rooms, size, additional fees (avgift), viewing time, and a link to the apartment listing.

Copy paste into a spreadsheet for further slice and dice. 

E.g.
```
Krysshammarvägen 44, 2 tr	4 195 000 kr	4 rum	89 m²	4 867 kr/mån	sön 21 maj kl 11:45	https://www.hemnet.se/bostad/lagenhet-4rum-vastra-skogen-solna-kommun-krysshammarvagen-44,-2-tr-19988435
Johan Enbergs väg 48A, 3 tr	5 350 000 kr	3 rum	80 m²	5 045 kr/mån	sön 21 maj kl 15:15	https://www.hemnet.se/bostad/lagenhet-3rum-vastra-skogen-solna-kommun-johan-enbergs-vag-48a,-3-tr-19800197
Krysshammarvägen 44, 2 tr	4 195 000 kr	4 rum	89 m²	4 867 kr/mån	sön 21 maj kl 11:45	https://www.hemnet.se/bostad/lagenhet-4rum-vastra-skogen-solna-kommun-krysshammarvagen-44,-2-tr-19988435
Storgatan 76B	5 995 000 kr	5 rum	122 m²	6 438 kr/mån	sön 21 maj kl 14:30	https://www.hemnet.se/bostad/lagenhet-5rum-huvudsta-solna-kommun-storgatan-76b-19973366
Wiboms väg 23	3 500 000 kr	3 rum	87 m²	5 286 kr/mån	sön 21 maj kl 13:00	https://www.hemnet.se/bostad/lagenhet-3rum-vastra-skogen-solna-kommun-wiboms-vag-23-19977495
Epistelvägen 1B	5 395 000 kr	3 rum	82 m²	4 442 kr/mån	sön 21 maj kl 14:50	https://www.hemnet.se/bostad/lagenhet-3rum-vastra-skogen-solna-kommun-epistelvagen-1b-19968125
Släggbacken 8	4 095 000 kr	3 rum	92 m²	4 886 kr/mån	sön 21 maj kl 12:30	https://www.hemnet.se/bostad/lagenhet-3rum-huvudsta-solna-kommun-slaggbacken-8-19973977
Jungfrudansen 27, vån 3	4 395 000 kr	4 rum	99 m²	6 062 kr/mån	sön 21 maj kl 11:30	https://www.hemnet.se/bostad/lagenhet-4rum-huvudsta-solna-kommun-jungfrudansen-27,-van-3-19930335
Johan Enbergs väg 54B	4 895 000 kr	3 rum	80 m²	5 045 kr/mån	sön 21 maj kl 15:15	https://www.hemnet.se/bostad/lagenhet-3rum-vastra-skogen-solna-kommun-johan-enbergs-vag-54b-19973084
Johan Enbergs väg 9, 3 tr	3 795 000 kr	2 rum	67 m²	3 131 kr/mån	sön 21 maj kl 12:45	https://www.hemnet.se/bostad/lagenhet-2rum-vastra-skogen-solna-kommun-johan-enbergs-vag-9,-3-tr-19970217
Bygatan 23	3 250 000 kr	3 rum	88 m²	4 825 kr/mån	sön 21 maj kl 13:00	https://www.hemnet.se/bostad/lagenhet-3rum-huvudsta-solna-kommun-bygatan-23-19973416
Armégatan 11A	3 250 000 kr	2 rum	62 m²	3 358 kr/mån	sön 21 maj kl 13:40	https://www.hemnet.se/bostad/lagenhet-2rum-huvudsta-ingenting-solna-kommun-armegatan-11a-19969043
Jungfrudansen 12, vån 5	4 695 000 kr	3,5 rum	87 m²	5 041 kr/mån	sön 21 maj kl 12:10	https://www.hemnet.se/bostad/lagenhet-3,5rum-huvudsta-solna-kommun-jungfrudansen-12,-van-5-19942317
Polhemsgatan 1	3 395 000 kr	2 rum	68 m²	2 909 kr/mån	sön 21 maj kl 12:45	https://www.hemnet.se/bostad/lagenhet-2rum-gamla-huvudsta-solna-kommun-polhemsgatan-1-19934371
Krysshammarvägen 32, 5 tr	4 695 000 kr	5 rum	108 m²	5 898 kr/mån	sön 21 maj kl 13:00	https://www.hemnet.se/bostad/lagenhet-5rum-vastra-skogen-solna-kommun-krysshammarvagen-32,-5-tr-19579396
Bygatan 17, vån 5	3 995 000 kr	3 rum	88 m²	4 825 kr/mån	sön 21 maj kl 13:40	https://www.hemnet.se/bostad/lagenhet-3rum-huvudsta-solna-kommun-bygatan-17,-van-5-19916280
Storgatan 52, 8tr	2 895 000 kr	2 rum	64,8 m²	3 072 kr/mån	sön 21 maj kl 14:30	https://www.hemnet.se/bostad/lagenhet-2rum-huvudsta-solna-kommun-storgatan-52,-8tr-19914956
Storgatan 62C, vån 5	4 995 000 kr	5 rum	103 m²	6 858 kr/mån	sön 21 maj kl 11:20	https://www.hemnet.se/bostad/lagenhet-5rum-huvudsta-solna-kommun-storgatan-62c,-van-5-19471998
Jonstorpsvägen 30	4 495 000 kr	4 rum	97 m²	5 834 kr/mån	sön 21 maj kl 11:00	https://www.hemnet.se/bostad/lagenhet-4rum-huvudsta-solna-kommun-jonstorpsvagen-30-19732821
```

## Dependencies
The script relies on the following Python libraries, which are listed in the requirements.txt file:

- cfscrape
- beautifulsoup4

These dependencies will be automatically installed during the installation process mentioned earlier.
