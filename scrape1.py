#import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

money = urlopen('https://www.bloomberg.com/quote/SPX:IND')
# print(money.read())

soup = BeautifulSoup(money, 'lxml')
name = soup.find('div', attrs={'class':''})