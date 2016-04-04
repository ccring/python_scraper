import requests
from bs4 import BeautifulSoup
import mysql.connector

search = raw_input("input a google seach term\n")

formatted_search = search.replace(" ", "+")

page_one = requests.get("https://www.google.com/search?q=%s" % formatted_search)
page_two = requests.get("https://www.google.com/search?q=%s&start=10" % formatted_search)

def get_link_headers(page):
    page_content = page.content
    parsed_content = BeautifulSoup(page_content, "html.parser")
    link_headers = parsed_content.find_all("h3", class_="r")
    return link_headers

link_headers_one = get_link_headers(page_one)
link_headers_two = get_link_headers(page_two)

del link_headers_one[0]

print "Here are the first twenty results of your search:\n"

for header in link_headers_one:
    result_link = header.a["href"][7:]
    link_content = requests.get(result_link).content
    parsed_link = BeautifulSoup(link_content, "html.parser")
    print result_link + "\n"
    print "Here is some relevant information from the above result:\n"
    sub_links = parsed_link.find_all("a")
    for anchor in sub_links:
        print "   " + anchor["href"]

# for header in link_headers_two:
#     result_link = header.a["href"][7:]
#     print result_link + "\n"
