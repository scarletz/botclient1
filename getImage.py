import requests
import sys
import os
from PIL import Image
from StringIO import StringIO
import shutil

#param
#mid(messageid),filenumber,dir
#

# image download
def download_image(url, timeout = 10):

    response = requests.get(url,allow_redirects=False, timeout=timeout)
    if response.status_code != 200:
        e = Exception("HTTP status: " + response.status_code)
        raise e

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response

# set filename
def make_filename(base_dir, number, url):
    if os.path.isdir(base_dir)==False:
        print "not exit image dir,make dir"
        os.mkdir(base_dir)

    ext = os.path.splitext(url)[1] # kakutyoushi
    filename = number        # number+kakutyoushi
    fullpath = os.path.join(base_dir, filename)
    #fullpath=filename
    return fullpath

def save_image(filename, r):
    print filename
    i = Image.open(StringIO(r.content))
    i.save(filename)


def test(subs=None):
    if subs == None:
        args = sys.argv
    
        if len(args)<=1:
            print "error:please set args1(num) return"
            return
        subs=args[1]
    url = "https://homeict.net/image/{mid}"
    url=url.replace("{mid}",subs)

    try:
        resp=download_image(url)
    except:
        import traceback
        traceback.print_exc()
        return "error"
    save_image(make_filename("image",subs,"a.jpg"),resp)
    return "ok"
if __name__ == '__main__':
    test()
