import commands
import re
#check = commands.getoutput("7_visualization.sh ../app")

#i=check.find("Error")
#if i!=-1:
#    print "already"
#else:
#    print "ng"
def test():
  c=commands.getoutput("docker ps") 
  i=c.find("50100")
  if i==-1:
    print "not run"
    return
  print "docker stops"
  
  pattern=re.findall('50100->8080\/tcp\s*\w*_\w*',c)
  if len(pattern)==0:
    print "no list"
    return

  pat2=re.findall('\w*_\w*',pattern[0])
  #print pat2[0]
  
  str="docker stop "+pat2[0]
  c=commands.getoutput(str)

  print c

if __name__ == '__main__':
  ret=test()
