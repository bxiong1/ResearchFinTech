import pandas as pd
import os
import numpy as np
from all_spacs_1 import all_SPACs

files = []
date = []
path = '/home/ubuntu/research/test/data'
datanames = os.listdir(path)
length = len(datanames)-1
for i in datanames:
	if os.path.splitext(i)[1]=='.tsv':
		if length >= 0:
			files.append(datanames[length])
			date.append(os.path.splitext(datanames[length])[0])
			length = length - 1

finaldata = all_SPACs(files)
