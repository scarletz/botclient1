import requests
import sys 
import time
import getImage
import os


import re
import codecs
 
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


  f = open('../intermediate/splittedGpsLog/Dammy.csv', 'w')
  f.write("LAT,LON,TIME,SPEED\n")
  lonlat=r.text.split(":")
  strs=lonlat[0]+","+lonlat[1]+",2018-05-11T04:53:05Z,60.335212\n"
  print strs
  f.write(strs)
  strs=lonlat[0]+","+lonlat[1]+",2018-05-11T04:53:15Z,100.335212\n"
  f.write(strs)
  strs=lonlat[0]+","+lonlat[1]+",2018-05-11T04:53:25Z,100.335212\n"
  f.write(strs)
#  strs=lonlat[0]+","+lonlat[1]+",2018-05-11T04:53:15Z,200.335212\n"
#  f.write(strs)
  f.close()
  os.system("2_filterVideo.sh ..")
  os.system("sudo rm ../intermediate/analysisFrames/frame00000.jpg")
  ret=os.system("sudo mv image/1.jpg ../intermediate/analysisFrames/frame00000.jpg")
  if ret!=0:
    return None

  os.system("3_segmentFrames.sh ..")
  os.system("4_caffeTest.sh ..")  
#  os.system("rm ../intermediate/analysisFramesGpsInfo.csv")
  
#  f = open('../intermediate/analysisFramesGpsInfo.csv', 'w')
#  f.write("NAME,LAT,LON,TIME1,TIME2\n")
#  lonlat=r.text.split(":")
#  strs="frame00000.jpg,"+lonlat[0]+","+lonlat[1]+",0,0\n"
#  f.write(strs)
#  f.close()
  os.system("5_estimateDamageLevel.sh ..")
  

  newText="LineData0"
  read_file = open("../parameter.yml", 'r')
  write_file = open("../parameter.yml.new", 'w')
  lines = read_file.readlines()
  lines2 = []
  for line in lines:
    line = line.replace("LineData",newText)
    lines2.append(line)
  else:
    write_file.write(''.join(lines2)) 
    read_file.close()
  
  os.system("rm  ../parameter.yml")
  os.system("mv ../parameter.yml.new ../parameter.yml")

  os.system("6_createVisData.sh ../ ../app")


  



  return 0

if __name__ == '__main__':
  for i in range(10):
    ret=test()
    if ret==0:
	break
    time.sleep(5)
