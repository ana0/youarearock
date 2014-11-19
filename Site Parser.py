from bs4 import BeautifulSoup
from urllib import *

cats = urlopen("http://www.oxforddictionaries.com/").read()

catscats = BeautifulSoup(cats)

print(catscats.prettify('utf-8'))
