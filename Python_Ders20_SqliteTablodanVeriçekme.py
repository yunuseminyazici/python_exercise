import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo2 (zaman REAL,tarih TEXT, anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle():      #Tabloya random deger atama
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime = "Python Sqlite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo2(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih, anahtarkelime, deger))
    con.commit()

def degerlerial():
    cursor.execute("SELECT  * FROM Tablo2")  #* olduğu için bütün satırları ve sütunların hepsini döndürür. eğer sadece zaman veya tarih almak istersek *yerine gerekli parametre yazılır
    #cursor.execute("SELECT  * FROM Tablo2 WHERE deger = 2.0") #sadece degeri 2.0 olan değerleri alır
    data = cursor.fetchall() #sorgudan dönen değerleri atamak
    for i in data:
        print(i)


degerlerial()
con.close()

