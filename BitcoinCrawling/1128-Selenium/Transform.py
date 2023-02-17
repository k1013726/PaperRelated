import pandas as pd
import time

df=pd.read_csv('origin_ethereum.csv')


for i in range(df.shape[0]):
    timeString = df['CoinDate'][i].replace(' ','') # 輸入原始字串
    struct_time = time.strptime(timeString,"%b%d,%Y") # 轉成時間元組
    df['CoinDate'][i]=time.strftime("%Y/%m/%d", struct_time)
    df['CoinOpen'][i]=float(df['CoinOpen'][i].replace('$','').replace(',',''))
    df['CoinHigh'][i]=float(df['CoinHigh'][i].replace('$','').replace(',',''))
    df['CoinLow'][i]=float(df['CoinLow'][i].replace('$','').replace(',',''))
    df['CoinClose'][i]=float(df['CoinClose'][i].replace('$','').replace(',',''))
    df['CoinVolume'][i]=float(df['CoinVolume'][i].replace('$','').replace(',',''))
    df['CoinCap'][i]=float(df['CoinCap'][i].replace('$','').replace(',',''))
df=df.drop("Unnamed: 0", axis = 1)
df.to_csv('ethereum_tran.csv')