from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#無痕設定
# opts = Options()
# opts.add_argument("--incognito")
# driver = webdriver.Chrome('chromedriver.exe',chrome_options=opts)


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://coinmarketcap.com/currencies/ethereum/historical-data/")
driver.maximize_window()


fina=[]
for i in range(60):
    try:
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/p[1]/button').click()        
    except:
        continue


fina=driver.find_elements(By.TAG_NAME,'td')
CoinDate=[]
CoinOpen=[]
CoinHigh=[]
CoinLow=[]
CoinClose=[]
CoinVolume=[]
CoinCap=[]

for i in range(int(len(fina)/7)):
    CoinDate.append(fina[7*i].text)
    CoinOpen.append(fina[7*i+1].text)
    CoinHigh.append(fina[7*i+2].text)
    CoinLow.append(fina[7*i+3].text)
    CoinClose.append(fina[7*i+4].text)
    CoinVolume.append(fina[7*i+5].text)
    CoinCap.append(fina[7*i+6].text)

Coin={'CoinDate':CoinDate,'CoinOpen':CoinOpen,'CoinHigh':CoinHigh,'CoinLow':CoinLow,'CoinClose':CoinClose,
'CoinVolume':CoinVolume,'CoinCap':CoinCap}
df=pd.DataFrame(Coin)
df.to_csv('origin_ethereum.csv')
print('done')

driver.close()