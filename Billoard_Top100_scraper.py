import requests
from bs4 import BeautifulSoup
import pandas as pd

#Requests object
req=requests.get("https://www.billboard.com/charts/hot-100").content
soup=BeautifulSoup(req,'html.parser')
main=soup.findAll('main',id='main')

position=[]
songs_names=[]
artist_names=[]
#Scraping Data
for i in main:
    charts=i.findAll('div',id="charts")
    for i in charts:
        names=i.findAll('span',class_="chart-element__information__artist text--truncate color--secondary")
        songs=i.findAll('span',class_="chart-element__information__song text--truncate color--primary")
        chart_number=i.findAll('span',class_="chart-element__rank__number")
        for i in chart_number:
            ranks=i.text
            position.append(ranks)
        for i in songs:
            song=i.text
            songs_names.append(song)
        for i in names:
            artist_name=i.text
            artist_names.append(artist_name)


print(position)
print(songs_names)
print(artist_names)
#Makin a pandas dataframe
pd_data_frame=pd.DataFrame({
    'Rank':position,
    'Song Name':songs_names,
    'Artist Name':artist_names
})
#Saving it to excel
file=pd.ExcelWriter('Billoard_Top_100.xlsx')

pd_data_frame.to_excel(file)
file.save()
