import requests
from bs4 import BeautifulSoup
import pandas as pd  
import time

from fake_useragent import UserAgent
import time
import json
import datetime


def date_to_timestamp(s,e):
    start = str(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))[:-2]
    end = str(time.mktime(datetime.datetime.strptime(e, "%d/%m/%Y").timetuple())+86400)[:-2]
    return [start,end]


Market_Cap=[]
BitcoinOpening=[]
Open=[]
Date=[]
High=[]
Low=[]
Volume=[]
Close=[]
coins=[]


for id in range(1,2):
    DataTime=date_to_timestamp('01/01/2020','28/11/2022')
    ua = UserAgent()
    user_agent = ua.random
    headers = {'user-agent': user_agent}
    url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id='+str(id)+'&convertId=2811&timeStart='+DataTime[0]+'&timeEnd='+DataTime[1]
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")


    history_data = json.loads(soup.contents[0])            
    quotes = history_data["data"]['quotes']  
    for quote in quotes:
        time.sleep(0.1)
        Market_Cap.append(quote["quote"]["marketCap"]) 
        Open.append(quote["quote"]["open"])
        struct_time = time.strptime(quote["quote"]["timestamp"][:10], "%Y-%m-%d") # 轉成時間元組
        Date.append(int(time.mktime(struct_time)))         
        High.append(quote["quote"]["high"])
        Low.append(quote["quote"]["low"]) 
        Volume.append(quote["quote"]["volume"])   
        Close.append(quote["quote"]["close"])
        coins.append(history_data["data"]["name"])



lo={'Cion':coins,'Market_Cap':Market_Cap,'Open':Open,'Date':Date,'High':High,'Low':Low,'Volume':Volume,'Close':Close}

df = pd.DataFrame(lo)
df.to_csv('data.csv')
