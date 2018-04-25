import requests

url = "https://homeict.net/upimage"
filename = "image/1.jpg"
files = {'upload_file': open(filename, "rb")}
res = requests.post(url, files=files)

