import pandas as pd
import requests
from bs4 import BeautifulSoup

file_path = '/Users/rishabhbhartiya/Desktop/TMKOC/1_1000/701_800.html'

with open(file_path, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all the episode details
episodes = soup.find_all('div', class_='episodeDetails')

# Extract the required information
episode_data = []
for episode in episodes:
    title = episode.find('span', class_='episodeTitle').text
    metadata = episode.find('div', class_='episodeMetadata').text
    description = episode.find('p', class_='description').text
    episode_data.append({
        'title': title,
        'metadata': metadata,
        'description': description
    })
    
df= pd.DataFrame(episode_data)
df.to_csv("TMKOC8.csv")

