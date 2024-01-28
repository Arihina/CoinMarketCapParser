from pprint import pprint

import bs4
import fake_useragent
import requests

ref = "https://coinmarketcap.com/"
header = {"user-agent": fake_useragent.UserAgent().random}

response = requests.get(ref, headers=header).text
soup = bs4.BeautifulSoup(response, 'lxml')

links = soup.find_all('a', class_="cmc-link")

token_links = [link for link in links if 'class="cmc-link" href="/currencies/' in str(link)]

pprint(token_links)

filter_links = {}