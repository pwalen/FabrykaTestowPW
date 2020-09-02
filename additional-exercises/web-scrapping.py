import requests
from bs4 import BeautifulSoup
import pandas as pd

# ! Download and parse the HIML

start_url = 'https://pl.wikipedia.org/wiki/Tesla,_Inc.'

# Download the HTML from start_url
downloaded_html = requests.get(start_url)

# Parse the HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text)

# Save a local copy
with open('downloaded_html', 'w') as file:
    file.write(soup.prettify())
