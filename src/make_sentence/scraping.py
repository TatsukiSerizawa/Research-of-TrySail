from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def get_entry_list(url):
    links = []
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    pages = soup.find_all('li', class_='skin-borderQuiet')
    for link in pages:
        #print(link.find("a").get("href"))
        links.append("https://ameblo.jp{}".format(link.find("a").get("href")))
    return links

def get_text(entry_list):
    sentence = []
    for html in entry_list:
        html = urlopen(html)
        soup = BeautifulSoup(html, "html.parser")
        all_text = soup.find_all("div", id='entryBody')
        for text in all_text:
            #print(text.find_all("p"))
            sentence.append(text)
    print("finish")
    return sentence
