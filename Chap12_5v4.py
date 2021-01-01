#Prog will use urlib to read HTML from data files below, extract hre= values from the anchor tags, scan for a tag that is in a paritcular position relative to the frist name in the list,
#follow that link and repeate the process a number of times and report the last name you findself.
#Site http://py4e-data.dr-chuck.net/known_by_Fikret.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
linkslist =[]


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
count = input('Enter Count: ')
position = input('Enter Position: ')
countint = int(count)
counter = countint
positionint = int(position) - 1
url1 = url
if countint > 0: #If count count is greater then 0
    html = urllib.request.urlopen(url1, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        alltags = tag.get('href', None)
        if len(alltags) != 0: #If they do find a link then append it to a list called Linkslist
                linkslist.append(alltags)
#        url2 = linkslist[positionint] #URl2 is the 3 URL on first pagem opened that and repeated process.
    counter = counter - 1
    print(linkslist[positionint]) #print 3rd link
    while counter > 0:
        #REPEAT PROCESS OPENING 3rd LINK
        html2 = urllib.request.urlopen(linkslist[positionint], context=ctx).read() #read Url2 now and repeat process
        linkslist =[]
        soup2 = BeautifulSoup(html2, 'html.parser')
        tags2 = soup2('a')
        for tag2 in tags2:
            alltags2 = tag2.get('href', None)
            if len(alltags2) != 0: #If they do find a link then append it to a list called Linkslist
                    linkslist.append(alltags2)
        url3 = linkslist[positionint]
        counter = counter - 1
        print(url3)# print 3rd link


else:
    print("Count shown was 0 or below")
