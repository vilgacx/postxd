#!/usr/bin/env python3
import sys
import requests
from alive_progress import alive_it
from bs4 import BeautifulSoup

post_url=input('Enter Post Link: ')
filename=str(sys.argv[1])
re=requests.get('https://redditsave.com/info?url='+post_url)

if re.status_code == 200:
    print('Connected')

    soup = BeautifulSoup(re.content, 'html.parser')
    file_url = ((soup.find_all('a',class_='downloadbutton'))[0])['href']
    
    r = requests.get(file_url, stream = True)
    with open(filename,"wb") as flw:
        for chunk in alive_it(r.iter_content(chunk_size=2048),title=f"Downloading {filename}"):
            if chunk:
                flw.write(chunk)
            else:
                print('Something went wrong.')

elif re.status_code == 400:
    print("Invalid Post Link.")
else:
    print('Something went wrong.')
