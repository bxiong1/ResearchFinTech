import pandas as pd
import regex as re
import numpy as np

def preprocess_data(name_split, a):
    for i in range(len(a)):
        if a[i].find(name_split) != -1:
            a[i] = a[i].replace(name_split, "")
        else:
            continue
    return a
    
