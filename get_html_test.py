 import pandas as pd 
import requests
import io
import sys
import urllib.request
from bs4 import BeautifulSoup
def html_text_test(name, url, num, num2):
    index=list()
    finals = list()
    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    #open the SEC report by using the url link
    r = requests.get(url, headers = header)
    html = r.text
    #use beautiful soup to find all html start with <p>
    bf = BeautifulSoup(html, "html.parser")
    texts = bf.find_all("p")
    if len(texts) == 0:
        print('Not Found!')
    else:
    #use the last name to allocate the paragragh we want in the SEC report
        f = open('text'+str(num2)+'(2).txt', 'w', encoding='utf-8')
        for i in range(len(name)):
            for j in range(len(texts)):
                if str(texts[j]).find(str(name[i])) != -1:
                    index.append(j)
                    
        #look for the special characters in utf-8 format when transformed into text files then get rid of these special characters.
        xa = u'\xa0'
        x2007 = u'\u2007'
        x2009 = u'\u2009'
        xn = u'\n'
        xs = u'/s/'
        for z in index:
            temp = texts[z].get_text()
            f.write(str(temp))
            f.write('\n')
        if len(index) ==0:
            for a in range(len(texts)):
                temp = texts[a].get_text()
                if xa in temp:
                    temp = temp.replace(u'\xa0',u' ')
                if x2007 in temp:
                    temp = temp.replace(u'\u2007',u' ')
                if x2009 in temp:
                    temp = temp.replace(u'\u2009',u' ')
                if xn in temp:
                    temp = temp.replace(u'\n',u' ')
                if xs in temp:
                    temp = temp.replace(u'/s/',u' ')
                f.write(str(temp))
                f.write('\n')
                f.write('\n')