import twint

c = twint.Config()
c.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

#搜尋使用者名稱貼文
# c.Username='BTCTN'

c.Search='bitcion'
c.Store_csv = True
c.Output = "BitcionSearch.csv"


# c.Since='2023-2-26'
# c.Until='2023-2-20'        
# c.Lang='en'
# c.Count=True

# Run
twint.run.Search(c)
