import requests as r
import bs4


base_url = 'https://www.amazon.in'
url = 'https://www.amazon.in/dp/B07JHDKXK4'
headers = {
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

base_response = r.get(base_url, headers=headers)
cookies = base_response.cookies

product_response = r.get(url, headers=headers, cookies=cookies)

soup = bs4.BeautifulSoup(product_response.text, features='lxml')
price_lines = soup.findAll(class_="a-price-whole")
print(price_lines[0])
