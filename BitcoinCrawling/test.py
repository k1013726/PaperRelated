# import time
# import datetime
# import pandas

# def date_to_timestamp(s,e):
#     start = str(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))[:-2]
#     end = str(time.mktime(datetime.datetime.strptime(e, "%d/%m/%Y").timetuple())+86400)[:-2]
#     return [start,end]


# print(date_to_timestamp("01/01/2021","02/10/2021")[0])


import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print('-'*80)
print("PATH:", os.environ.get('PATH'))