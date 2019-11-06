# coding:utf-8
import re

import requests
from bs4 import BeautifulSoup


def get_entry_list(html):
    url_list = [html]
    while True:
        html = requests.get(html).content
        soup = BeautifulSoup(html, "lxml")
        next_page = soup.find("a", {"class", "skinSimpleBtn pagingNext"})
        if isinstance(next_page, type(None)):
            print("finish")
            return url_list
        else:
            url_list.append(next_page["href"])
            html = next_page["href"]


def get_url(entry_list):
    page_list = []
    for html in entry_list:
        html = requests.get(html).content
        soup = BeautifulSoup(html, "lxml")
        text = soup.find_all("a", {"class", "contentTitle"})
        page_list.append(text)
    print("finish")
    return page_list


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def scraping(all_entry_list, BASE_DIRE):
    for entry_list in all_entry_list:
        for url in entry_list:
            title = url.string
            with open("{dir}{title}.txt".format(dir=BASE_DIRE, title=title), "w") as file:
                html = requests.get(url["href"]).content
                soup = BeautifulSoup(html, "lxml")
                div_text = soup.find("div", {"class", "articleText"})
                text = cleanhtml(str(div_text)).strip()
                print("Written file: {0}.txt".format(title))
                file.write(text)
    print("finish")