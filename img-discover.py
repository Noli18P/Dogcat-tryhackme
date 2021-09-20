#/usr/bin/python3
#author: Martin Mtz

import requests
import sys
import signal

def exit(sig,frame):
    print("\n [!] Wait...")
    sys.exit(1)

#ctrl c
signal.signal(signal.SIGINT, exit)

def make_request():
    print('Loocking for images....')

    for i in range(20):
         url = 'http://10.10.178.148/dogs/x.jpg'.replace('x', str(i)) 
         r = requests.get(url)
         if r.status_code == 200:
             print('The image', url, ' exists')
         else:
             print('The image', url, ' does NO exists')
    
    print('\n [!]Now the cats...')

    for i in range(20):
         url = 'http://10.10.178.148/cats/x.jpg'.replace('x', str(i)) 
         r = requests.get(url)
         if r.status_code == 200:
             print('The image ', url, ' exists')
         else:
             print('The image', url, ' does NO exists')   


if __name__ == '__main__':
    make_request()
