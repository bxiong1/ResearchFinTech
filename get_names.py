import pandas as pd
import requests
import io
import sys
import urllib.request
from bs4 import BeautifulSoup
from get_html_text import html_text
from parse_name import last_name
from get_html_test import html_text_test
fUrl = open('url3.txt', 'r')
num = 43
num2 = 43
for line in fUrl:
    name_list = list()
    fName = pd.read_csv('result'+str(num)+'.csv')
    #read in the csv files and grab the corresponding last names of member
    for i in range(len(fName['0'])):
        if fName['0'].iloc[i] == 'Name' or fName['0'].iloc[i] == '' or fName['0'].iloc[i]=='NAME':
            continue
        else:
            name_list.append(fName['0'].iloc[i])
    last_name_list=last_name(name_list)
    print(last_name_list)
    print(num)
    #pass in the last names in order to find the corresponding contents texts(background information) in SEC reports
    html_text_test(last_name_list,line,num,num2)
    num = num +1
    num2 = num2 +1