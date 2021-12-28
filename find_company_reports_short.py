import pandas as pd
# This is a general function to find the selected report and selected company in one single SEC report
def find_company_reports_init(files, selectedcompany, selectedreport,alternatedreport,f):
	csv = pd.read_csv(files[f], sep='\t', lineterminator = '\n', names = None)
	csv.columns.values[0] = 'Item'
	companyreport = csv[(csv['Item'].str.contains(selctedcompany)) & (csv['Item'].str.contains(selectedreport))]
	if companyreport.empty:
		companyreport = csv[(csv['Item'].str.contains(selectedcompany)) & (csv['Item'].str.contains(alternatedreport))]
	return companyreport
# This is a general function to find the selected report and selected company in variety of SEC reports
def find_company_reports(files, selectedcompany, selectedreport):
	for f in range(0,len(files)):
		csv = pd.read_csv(files[f], sep='\t', lineterminator = '\n', names = None)
		csv.columns.values[0] = 'Item'
		companyreport = csv[(csv['Item'].str.contains(selectedcompany, case = False)) & (csv['Item'].str.contains(selectedreport))]

		if companyreport.empty:
			continue
		else:
			index = f
			break
	return companyreport
#This is a general function to standarize some of the company names ending.
def corner_cases(files, selectedcompany, selectedreport,namebefore,nameafter):
	if selectedcompany.find(namebefore) == -1:
		pass
	else:
		selectedcompany = selectedcompany.replace(namebefore, nameafter)
	company_reports = find_company_reports(files, selectedcompany, selectedreport)
	return company_reports
