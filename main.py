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

print("Currencies from the site https://coinmarketcap.com/")

for key in currencies.keys():
    print(key)

currency_name = input("Select a currency name ")

if currency_name in currencies.keys():
    currency_link = currencies[currency_name]
    response = requests.get(currency_link, headers=header).text
    soup = bs4.BeautifulSoup(response, 'lxml')

    price = str(soup.find('span', class_="sc-f70bb44c-0 jxpCgO base-text"))
    price = price[price.find('>') + 1:price.rfind('<'):]

    name = str(soup.find('span', class_="sc-f70bb44c-0 jltoa"))
    name = name[name.find('>') + 1:name.rfind('<span'):]

    print(f"{name=}, {price=}, {currency_link=}")
else:
    print("The currency was not found")
