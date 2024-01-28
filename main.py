import bs4
import fake_useragent
import requests

ref = "https://coinmarketcap.com/"
header = {"user-agent": fake_useragent.UserAgent().random}

response = requests.get(ref, headers=header).text
soup = bs4.BeautifulSoup(response, 'lxml')

links = soup.find_all('a', href=lambda link: link and link.startswith("/currencies/"))

currencies_links = {str(link)[str(link).find('<'):str(link).find('>') + 1:] for link in links}

currencies_links = list({link[link.find('/') + 1:link.rfind('/') + 1:] for link in currencies_links})

currencies = {value[value.find('/') + 1:value.rfind('/'):]: ref + value for value in currencies_links}
