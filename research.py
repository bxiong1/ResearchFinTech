import pandas as pd
import os
import edgar
edgar.download_index("/root/test/data", 2012, "MyCompany edward@mycompany.com", skip_all_present_except_last=False)

files = []
date = []
path = '/root/test/data'
datanames = os.listdir(path)
length = len(datanames)-1
for i in datanames:
	if os.path.splitext(i)[1]=='.tsv':
		if length >= 0:
			files.append(datanames[length])
			date.append(os.path.splitext(datanames[length])[0])
			length = length - 1


