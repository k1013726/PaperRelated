import requests
from bs4 import BeautifulSoup
import pandas as pd  
import datetime
from google.cloud import bigquery
import os
from google.oauth2 import service_account

ItemList=['LME-Steel-Scrap-CFR-Turkey-Platts','LME-Steel-CFR-Taiwan-Argus','LME-Steel-CFR-India-Platts',
'LME-Steel-HRC-NW-Europe-Argus','LME-Steel-HRC-N-America-Platts','LME-Steel-HRC-FOB-China-Argus',
'LME-Steel-Rebar-FOB-Turkey-Platts','LME-Steel-Scrap-CFR-Turkey-Platts']

DateTime=[]
ItemName=[]
ItemPrice=[]

for Item in ItemList: 
    url='https://www.lme.com/en/Metals/Ferrous/'+Item
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html5lib")
    DateTime.append(str(datetime.date.today()))
    ItemName.append(soup.find_all('h1')[0].getText().strip())
    ItemPrice.append(float(soup.find_all('span',class_="hero-metal-data__number")[0].getText().strip()))

  
Price_dataframe={'DateTime':DateTime,'ItemName':ItemName,'ItemPrice':ItemPrice}
df = pd.DataFrame(Price_dataframe)
# df.to_csv('data.csv')


credentials = service_account.Credentials.from_service_account_file('steel-price-d1b32df1752d.json')
	
client = bigquery.Client(credentials=credentials)

table_id = 'steel-price.LME_Price.main'
 
job = client.load_table_from_dataframe(df, table_id)
job.result()  #等待寫入完成

table = client.get_table(table_id)
print(f'已存入{table.num_rows}筆資料到{table_id}')