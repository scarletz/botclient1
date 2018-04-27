import requests
import sys 
import time
import getImage

def test():
  args=sys.argv

  url="https://homeict.net/location/"+args[1]
  r=requests.get(url)

  index =r.text.find("Cannot")
  if index!=-1:
    print "not data"
    return
  print r.text
  ret=getImage.test("2.jpg")
  if ret=="error":
    print "image download error"
    return
  else:
    print "download image"

  

if __name__ == '__main__':
  for i in range(10):
    test()
    time.sleep(5)
