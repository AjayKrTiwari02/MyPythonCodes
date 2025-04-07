import urllib.request
from re import findall

url="https://www.summet.com/dmsi/html/codesamples/addresses.html"

a=urllib.request.urlopen(url)
html=a.read()
htmlstr=html.decode()
phn=findall("\(\d{3}\) \d{3}-{d{4}}",htmlstr)

for i in phn:
    print(i)