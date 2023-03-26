import twint

c = twint.Config()
#Bitcoin News
c.Username='BTCTN'
c.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"


c.Format = "ID {id} | Username {username}"

# c.Lang='en'
# c.Since='2014-10-27'
# c.Until='2023-2-28'            
c.Store_csv = True
c.Output = "BitcionSearch.csv"
c.Count=True
c.Limit=20
# Run
twint.run.Search(c)
