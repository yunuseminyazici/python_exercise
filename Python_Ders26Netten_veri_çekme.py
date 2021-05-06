cmdye ilk olarak python yazılır.
import requests
from bs4 import BeautifulSoup
r = requests.get(https://yellowpages.com.tr/) #url içindeki kaynağı html kodlarını alır
r.content #sayfa kaynağını gösterir
soup = BeautifulSoup(r.content) #daha düzgün görebilmek için
print(soup.prettify()) #sayfa kaynağını güzelleştir
soup.find_all("a") #sayfadaki etiketleri alır htmlde etiket a ile tanımlanır
linkler = soup.find_all("a")  #linkleri yazdırmak için
for link in linkler:
    print(link)

for link in linkler: #kaç tane link olduğunu görmek için
    print(link.get("href"))

for link in linkler: #linklere basılınca oluşan textler
    print(link.text)

for link in linkler: #linke basılınca gittiği yeri gösterir.
    print(link.text,link.get("hyref"))