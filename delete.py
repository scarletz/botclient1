import requests
import sys 
import time
import getImage
import os

import re
import codecs
 
def test():

  url="https://homeict.net/api/deleteL?num=loc.txt"
  r=requests.get(url)

  url="https://homeict.net/api/deleteI?num=1.jpg"
  r=requests.get(url)

if __name__ == '__main__':
  for i in range(10):
    ret=test()
