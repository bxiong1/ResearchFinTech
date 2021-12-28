import pandas as pd
import regex as re
import numpy as np
import requests
import csv
fUrl = open('url2.txt', 'r')
num = 44
for line in fUrl:
    if len(line) == 0:
        continue
    else:
    #Setting headers to access the contents on SEC webpage
        header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(line, headers = header)
        #grab all the tables from each SPAC report
        df = pd.read_html(r.text)
        for i in range(len(df)):
        #Find the corresponding team member tables in the report by looking for the key words and save it in csv file
            try:
                age = df[i].iloc[0].str.contains("Age", na = False)
                name = df[i][0].str.contains("Name", na = False)
                ages = df[i].iloc[0].str.contains("AGE", na = False)
                names = df[i][0].str.contains("NAME", na = False)
            except AttributeError:
                pass
            if name.any() or age.any():
                print(1)
                index = i
                break
            elif names.any() or ages.any():
                print(2)
                index = i
                break
            elif name.any() and age.any():
                index = i
                break
            elif names.any() and ages.any():
                index = i
                break
        df_data = pd.DataFrame()
        df_data = df_data.append(df[index])
        df_data=df_data.dropna(thresh = len(df_data) - 3, how = "all", axis = 1)
        df_data.to_csv('result'+str(num)+'.csv', index=False, encoding='utf-8')
        print('done')
        num = num+1

fUrl.close()
