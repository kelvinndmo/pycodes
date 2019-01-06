from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('novak.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in  soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div',class_='entry-content' ).p.text
    print(summary)

    video_source = article.find('iframe', class_='youtube-player')['src']


    vid_id = video_source.split('/')[4]


    vid_id = vid_id.split('?')[0]


    ##yotube link format
    yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    print(yt_link)
    
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()