import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import time
import datetime
import json


def date_to_timestamp(s,e):
    start = str(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))[:-2]
    end = str(time.mktime(datetime.datetime.strptime(e, "%d/%m/%Y").timetuple())+86400)[:-2]
    return start ,end

def coinmarketcap(start_date,end_date):
    url = 'https://coinmarketcap.com'
    response = rq.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data= soup.find('script',id="__NEXT_DATA__",type="application/json")

    coins={}
    coin_data=json.loads(data.contents[0])
    listings=coin_data["props"]["initialState"]["cryptocurrency"]['listingLatest']['data']
    for i in listings[1:3]:  #這邊可以決定要爬取幾個幣種[1:(2-101)]
        coins[str(i[8])]=i[15]

    start , end = date_to_timestamp(start_date,end_date) 

    percent=0
    total=100

    for coin in coins:
        Market_Cap=[]
        Open=[]
        High=[]
        Low=[]
        Volume=[]
        Close=[]
        Date=[]
        
        #print(coins[coin]+" historical data")
       
            
        url="https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id="+coin+"&convertId=2781&timeStart="+start+"&timeEnd="+end
        #url="https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?id="+coin+"&convert=USD&time_start="+start+"&time_end="+end
        response = rq.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        history_data = json.loads(soup.contents[0])
        quotes = history_data["data"]['quotes']
        for quote in quotes:
            time.sleep(0.01)
            Market_Cap.append(quote["quote"]["marketCap"])
            Open.append(quote["quote"]["open"])
            Date.append(quote["quote"]["timestamp"][:10])
            High.append(quote["quote"]["high"])
            Low.append(quote["quote"]["low"])
            Volume.append(quote["quote"]["volume"])
            Close.append(quote["quote"]["close"])
        
        lo={'Market_Cap':Market_Cap,'Open':Open,'Date':Date,'High':High,'Low':Low,'Volume':Volume,'Close':Close}

        df = pd.DataFrame(lo)
        df.to_csv('data.csv')
    
coinmarketcap("01/01/2021","02/10/2021")           
        