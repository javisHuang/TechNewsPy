'''
Created on 2021年8月27日

@author: x550v
'''

import webview
import time
import urllib.request
from bs4 import BeautifulSoup

htmlfileurl = '../assets/index.html'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
datarows = []
        
url = "https://www.ithome.com.tw/news"
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
html_cont = response.read()
soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
#print(soup.prettify())

content = soup.select('div .channel-item')
for t in content:
    row = {}
    title = t.select(".title")
    for t2 in title:
        a = t2.find('a')
        row['title'] = a.text
        row['href'] = "https://www.ithome.com.tw/"+a.get('href')
        datarows.append(row)
        
url = "https://buzzorange.com/techorange"
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
html_cont = response.read()
soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')

content = soup.select('div .post--vertical-3i_row .post__title')
for t in content:
    row = {}
    a = t.find('a')
    row['title'] = a.text
    row['href'] = a.get('href')
    datarows.append(row)
        


#for row in datarows:
#    print(row)

class Api:
    def getData(self):
        response = {
            "datarows":datarows
        }
        return response
    
def reload(window):
    window.load_url(htmlfileurl)
        
        
if __name__ == '__main__':
    api = Api()
    window = webview.create_window('hello', htmlfileurl, js_api=api)
    webview.start(reload, window, http_server=True)
