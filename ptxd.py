#!/usr/bin/env python3
import sys
import random
import requests
from alive_progress import alive_it
from bs4 import BeautifulSoup

post_url=str(sys.argv[1])
reddit=requests.get('https://redditsave.com/info?url='+post_url)
insta=requests.post('https://www.w3toys.com/',{'link':post_url,'submit':'DOWNLOAD'})
#fb=requests.get()
#twitter=requests.get()

def main(file_url):
    filetype=''

    if 'mp4' in file_url:
        filetype = 'mp4'
    elif 'png' in file_url:
        filetype = 'png'
    elif 'jpg' in file_url:
        filetype = 'jpg'
    elif 'jpeg' in file_url:
        filetype = 'jpeg'

    r = requests.get(file_url, stream = True)
    with open((str(random.randint(1,10000))+'.'+filetype),"wb") as flw:
        for chunk in alive_it(r.iter_content(chunk_size=2048),title=f"Downloading.."):
            if chunk:
                flw.write(chunk)
            else:
                print('Something went wrong.')

if "www.reddit.com" in list(post_url.split('/')):
    if reddit.status_code == 200:
        soup = BeautifulSoup(reddit.content, 'html.parser')
        redditxd = (((soup.find_all('a',class_='downloadbutton'))[0])['href'])
        #for i in redditxd:
        main(redditxd)
    elif reddit.status_code == 404:
        print("Invalid Post Link.")
elif "www.instagram.com" in list(post_url.split('/')):
    soup = BeautifulSoup(insta.content,'html.parser')
    instaxd = soup.find_all('a',attrs={'rel':'noopener noreferrer'})
    for i in instaxd:
        main(i['href'])
else:
    print('Something went wrong') 
