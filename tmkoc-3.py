# -*- coding: utf-8 -*-
"""tmkoc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Cr6IhVqsBExYfYivJPizMpjiscTHIXn
"""

import numpy as np
import pandas as pd

data = pd.read_csv('TMKOC11.csv')

data = data.drop('Unnamed: 0', axis=1)

def remove_substring(s):
  if "Taarak Mehta Ka Ooltah Chashmah" in s:
    s=  s.replace("Taarak Mehta Ka Ooltah Chashmah", "")
    parts = s.split(".")
    return int(parts[0])
  return s

data["new_title"] = data["title"].apply(remove_substring)

data.rename(columns={'new_title': 'episode_number'}, inplace=True)

def remove_string(t):
  if "Taarak Mehta Ka Ooltah Chashmah" in t:
    t=  t.replace("Taarak Mehta Ka Ooltah Chashmah", "")
    parts = t.split(".")
    return parts[1]
  return t

data["Episode_title"] = data["title"].apply(remove_string)

def remove_sign(sn):
  if "–" in sn:
    sn=  sn.replace("–", "")
  return sn

data["Episode_title"] = data["Episode_title"].apply(remove_sign)

def extract_runtime(rn):
  if "FULL_HD2" in rn:
    rn=  rn.replace("FULL_HD2", "")
    #return rn
  return rn

data["Runtime"] = data["metadata"].apply(extract_runtime)

data = data.drop(['metadata', 'title'], axis=1)

def Upload_date(Ud):
  Ud= Ud.split("mins")
  return Ud[1]

data["Released_on"] = data["Runtime"].apply(Upload_date)

def Upload_runtime(Ur):
  Ur= Ur.split("mins")
  return Ur[0]+"mins"

data["Episode_runtime"] = data["Runtime"].apply(Upload_runtime)

data.drop('Runtime', axis=1, inplace=True)

new_order = ['episode_number', 'Episode_title', 'description', 'Episode_runtime', 'Released_on']
data = data[new_order]

data.head(3)

data.info()



