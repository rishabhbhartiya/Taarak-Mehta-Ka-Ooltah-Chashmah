# -*- coding: utf-8 -*-
"""TaarakMehtaEpisodes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fIXN5O-lfJ3z-3NZFGEDqFUWnTVYYhId
"""

import numpy as np
import pandas as pd

# Load the dataset
data = pd.read_csv('TMKOC41.csv')

# Drop the unnecessary column
data = data.drop(columns='Unnamed: 0')

# Define functions to clean and transform the data
def extract_episode_number(s):
    if "Taarak Mehta Ka Ooltah Chashmah" in s:
        parts = s.replace("Taarak Mehta Ka Ooltah Chashmah", "").split(".")
        return int(parts[0])
    return s

def extract_episode_title(t):
    if "Taarak Mehta Ka Ooltah Chashmah" in t:
        parts = t.replace("Taarak Mehta Ka Ooltah Chashmah", "").split(".")
        return parts[1].replace("–", "").strip()
    return t

def extract_runtime(rn):
    return rn.replace("FULL_HD2", "")

def extract_release_date(Ud):
    return Ud.split("mins")[1].strip()

def extract_episode_runtime(Ur):
    return Ur.split("mins")[0].strip() + " mins"

# Apply transformations
data['episode_number'] = data['title'].apply(extract_episode_number)
data['Episode_title'] = data['title'].apply(extract_episode_title)
data['Runtime'] = data['metadata'].apply(extract_runtime)
data['Released_on'] = data['Runtime'].apply(extract_release_date)
data['Episode_runtime'] = data['Runtime'].apply(extract_episode_runtime)

# Drop unnecessary columns
data = data.drop(columns=['metadata', 'title', 'Runtime'])

# Reorder columns
new_order = ['episode_number', 'Episode_title', 'description', 'Episode_runtime', 'Released_on']
data = data[new_order]

df = pd.DataFrame(data)
data = df.sort_values(by='episode_number').reset_index(drop=True)

data.to_csv('TMKOC_EPISODES_41.csv', index=False)