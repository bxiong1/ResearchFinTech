import pandas as pd
import regex as re
import numpy as np
import requests
from data_process_2 import preprocess_data
from find_company_reports_short import find_company_reports, corner_cases
def all_SPACs(files):
	spac = pd.read_csv('SPACs.csv', names = None)
	a = spac.iloc[:,1]
	
	a = preprocess_data(" - Class A", a)
	a = preprocess_data(" Class A", a)
	a = preprocess_data(" Series A", a)
	a = preprocess_data(" , Inc.", a)
	spac['Name'] = a

	finaldata = []
	
	for j in range(len(spac)):
		selectedcompany = spac.iloc[j][1]
		selectedreport = "S-1"
		companyreport = find_company_reports(files, selectedcompany, selectedreport)
		Filing = companyreport['Item'].str.split('|')
		Filing = Filing.to_list()
		
		if len(Filing) == 0:
			companyreport = corner_cases(files, selectedcompany, selectedreport, "Limited", "Ltd")
			Filing = companyreport['Item'].str.split('|')
			Filing = Filing.to_list()
		if len(Filing) == 0:
			companyreport = corner_cases(files, selectedcompany, selectedreport, "Corporation", "Corp")
			Filing = companyreport['Item'].str.split('|')
			Filing = Filing.to_list()
		k = 0
		for i in range(len(Filing)):
			if Filing[i][2]=='S-1':
				k = i
		for item in Filing[k]:
			if 'html' in item:
				report = item
	
		url = 'https://www.sec.gov/Archives/' + report[:-1]
		header = {
		  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		  "X-Requested-With": "XMLHttpRequest"
		}

		r = requests.get(url, headers=header)
		df = pd.read_html(r.text)	

		document_index = df[0][df[0]['Type'].notna()]
		document_name = document_index[document_index['Type'].str.contains(selectedreport)]
		document_name=document_name['Document'].str.split(' ')
		document_name=document_name[0][0]
		report_formatted = report.replace('-','').replace('index.html','')
		url = 'https://www.sec.gov/Archives/' + report_formatted+ '/' +document_name
		
		header2 = {
		  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		  "X-Requested-With": "XMLHttpRequest"
		}

		r2 = requests.get(url, headers=header2)
		df = pd.read_html(r2.text)
                print(url)
                # for i in range(len(df)):
			# try:
				# age = df[i].iloc[0].str.contains("Age", na = False)
				# name = df[i][0].str.contains("Name", na = False)
			# except AttributeError:
				# pass
			# if age.any() or name.any():
				# index = i
				# break
		# df_data = df[index]
		# df_data = df_data.dropna(thresh = len(df_data) - 3, how = "all", axis = 1)
		# df_data = df_data.dropna(axis = 0)
		# df_data.columns = df_data.iloc[0]
		# df_data = df_data.drop(df_data.index[0])
	
		# finaldata.append(df_data)
	# return finaldata

