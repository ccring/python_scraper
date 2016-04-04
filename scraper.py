import requests
from bs4 import BeautifulSoup

request = requests.get("Https://www.google.com/search?q=cute+cats")

content = request.content

parsed_content = BeautifulSoup(content, "lxml")

print parsed_content.prettify()
