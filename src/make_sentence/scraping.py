from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = 'https://ameblo.jp/natsukawashiinablog/entrylist.html'

#response = requests.get(url)

def get_entry_list(url):
    links = []
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    pages = soup.find_all('li', class_='skin-borderQuiet')
    for link in pages:
        #print(link.find("a").get("href"))
        links.append(link.find("a").get("href"))
    return links


'''
# 出力フォーマットの定義
columns = ['title', 'url']
df = pd.DataFrame(columns=columns)

# スクレイピング先URL
url = 'https://ameblo.jp/natsukawashiinablog/entrylist.html'
#url = 'https://dividable.net/'
  
# ブログ記事取得
def getTargetPageData(targetUrl):
  print(targetUrl)
  html = urlopen(targetUrl)
  soup = BeautifulSoup(html, 'html.parser')
  entries = soup.find_all('li', class_='skin-borderQuiet')
  #entries = soup.find_all('div', class_='col-xs-12 wrap')
  global df

  print(entries)

  for entry in entries:
      se = pd.Series([
          entry.find('h2').find('a').get('title'),  #title
          entry.find('h2').find('a').get('href') #url
      ], columns)
      df = df.append(se, columns)

      
  nextPage = soup.find('div', class_='pull-right')   
  nextPageUrl = nextPage.find('a')
  if nextPageUrl:
    getTargetPageData(nextPageUrl.get('href'))
  else:
    print('Done')

if __name__ == '__main__':
  getTargetPageData(url)
  
  # 取得したデータを表示
  df

'''