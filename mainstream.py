import requests
import sys 
import time
import getImage
import os
def test():
  args=sys.argv

  url="https://homeict.net/location/"+"loc.txt"
  r=requests.get(url)

  index =r.text.find("Cannot")
  if index!=-1:
    print "not data"
    return None
  print r.text
  ret=getImage.test("1.jpg")
  if ret=="error":
    print "image download error"
    return None
  else:
    print "download image"
  os.system("rm ../intermediate/analysisFrames/frame00000.jpg")
  ret=os.system("mv image/1.jpg ../intermediate/analysisFrames/frame00000.jpg")
  if ret!=0:
    return None
  
  os.system("3_segmentFrames.sh ..")
  os.system("4_caffeTest.sh ..") 
  return 0
if __name__ == '__main__':
  for i in range(10):
    ret=test()
    if ret==0:
	break
    time.sleep(5)
