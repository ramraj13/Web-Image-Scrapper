from bs4 import  *
import requests as r
import os
from urllib.request import urlopen
import re
import sys

flag='https://comics.8muses.com'

r1=r.get('https://comics.8muses.com/comics/album/Blacknwhitecomics_com-Comix/BlacknWhiteComics/Housewives-of-Beaverton',params=None)
soup=BeautifulSoup(r1.text,"html.parser")
div=soup.findChildren('div',{'class':re.compile('image')})
links=[]
for i in div:
    links.append(i)

img=[]
for index,img_link in enumerate(links):
    if  index%2!=0:
        img.append(img_link)
final_link=[]

def img_extraction(link_img):
    images=str(link_img)
    image_s=images.split('"')

    for index_link in image_s:
        if len(index_link)> 15:
            return index_link

for item in img:
    final_link.append(img_extraction(item))

os.mkdir(sys.argv[1])

for indexes,image in enumerate(final_link):
    final_test_link=flag+image
    test=final_test_link.split('th')
    final_image_link=test[0]+"fl"+test[1]
    print(final_image_link)
    img_data=r.get(str(final_image_link)).content

    with open(sys.argv[1]+"/"+str(indexes+1)+'.jpg','wb+')as f:
        f.write(img_data)

    f.close()

