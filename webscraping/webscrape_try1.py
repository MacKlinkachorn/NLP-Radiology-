#File: webscrape_try1.py
#First try at web parsing for potential use in definition scraping.
#Following tutorial at https://www.youtube.com/watch?v=XQgXKtPSzUI

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

curr_url = 'https://simple.wikipedia.org/wiki/Natural_language_processing'

uClient = uReq(curr_url)
page_html = uClient.read()
uClient.close()

#html parting
page_soup = soup(page_html, "html.parser")