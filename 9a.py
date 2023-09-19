import requests 
import os
from bs4 import BeautifulSoup
#LINK for web
url='https://xkcd.com/l/'
#Folder creation
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')
    #Comic loop
    while True:
        #Download vcontent
        res=requests.get(url)
        res.raise_for_status
        #split page content using beautiful soup
        soup=BeautifulSoup(res.text, 'html.parser')
        #Find comic img URL
        comic_elem=soup.select('#comic_img')
        if comic_elem==[]:
            print("No image")
        else:
            comic_url='https:'+comic_elem[0].get('src')
            #download images
            print(f'Downloading images{comic_url}')
            res=requests.get(comic_url)
            res.raise_for_status()
            #save images to folder
            image_file=open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
                image_file.close()

            #URL of previous comic
            prev_link=soup.select('a[rel="prev"]')[0]
            if not prev_link:
                break
            url='https://xkcd.com'+prev_link.get('href')
            print("all comics downloaded")