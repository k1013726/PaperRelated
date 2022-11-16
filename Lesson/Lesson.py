# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import codecs

Contents=['agriculture','development','economics','education','science','makingnation']

for Contents in Contents:
    if not os.path.isdir(Contents):os.makedirs(Contents)
    for id in range(1,46,1):
        url='https://englishteststore.net/voa/'+Contents+'/lesson'+str(id)+'.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html5lib")
        with codecs.open((Contents+'/Lesson'+str(id)+'.text'), 'w+',"utf-8") as f:        
            f.write(soup.find_all('div',id='text1')[0].find_all('b')[2].getText())
            f.write('\n')
            f.write(soup.find_all('textarea')[0].getText())
