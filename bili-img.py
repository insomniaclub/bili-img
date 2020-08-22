#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import os

path = os.path.expanduser('~') + '/Pictures/'

def get_img(vid):
    print('Start finding the picture of ' + vid)
    res = requests.get('https://www.bilibili.com/video/' + vid + '/')
    res.encoding = res.apparent_encoding
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all(name='meta')[10]
    img_addr = item.get('content')

    print('Find the picture\'s address: ' + img_addr)
    try:
        img = requests.get(img_addr)
    except:
        print('The video does not exist!')
    else:
        print('Start downloading the picture ... ')
        with open(path + vid + '.jpg', 'wb') as file:
            file.write(img.content)
        print('Download Finished!')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('No av or bv number input!')
    else:
        get_img(sys.argv[1])
