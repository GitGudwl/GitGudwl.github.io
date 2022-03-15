from array import array
from pickle import APPEND
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

page = requests.get("https://republika.co.id/")
now = datetime.now()
obj = BeautifulSoup(page.text,'html.parser')

print(obj.title.text)


print ('\nMenampilkan semua teks headline')
print ('=================================')
for headline in obj.find_all('div',class_='conten1'):
    print (headline.find('h2').text)
    
print('\nMenampilkan kategori')
print('========================')
for kategori in obj.find_all('div',class_='teaser_conten1_center'):
        print(kategori.find('a').text)

print('\nMenampilkan waktu publish')
print('========================')
for publish in obj.find_all('div',class_='date'):
        print(publish.text)

current_time = now.strftime("%H:%M:%S")

print('\nMenampilkan waktu scrapping')
print('========================')
print("Waktu scrapping = ", current_time)       

data=[]

f=open('D:\Kuliah\proyek 1 pengembangan aplikasi dekstop\Personal Static web\publish.json','w')
for publish in obj.find_all('div',class_='conten1'):

    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktu_publish":publish.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})

jdumps=json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()