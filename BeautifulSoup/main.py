import requests


url="https://timesofindia.indiatimes.com/india/delhi"

r=requests.get(url)
# print(r.text)


#  To save in file :

def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)
        print(r.text)

# url="https://timesofindia.indiatimes.com/india/delhi"

fetchAndSaveToFile(url,"data/time7.html")

# https://timesofindia.indiatimes.com/city/delhi





