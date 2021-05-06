import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL,tarih TEXT, anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle():      #Tabloya random deger atama
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime = "Python Sqlite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih, anahtarkelime, deger))
    con.commit()

tabloolustur()
i = 0                #10 tane veri oluşturur.
while i<10:
    rastgeledegerekle()
    time.sleep(1)  #zamanı görebilmek için delay koyduk
    i += 1
con.close()