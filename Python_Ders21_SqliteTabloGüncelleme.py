import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo3 (zaman REAL,tarih TEXT, anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle():      #Tabloya random deger atama
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime = "Python Sqlite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo3(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih, anahtarkelime, deger))
    con.commit()

def degerlerial():
    cursor.execute("SELECT  * FROM Tablo3 WHERE deger = 2.0") #sadece degeri 2.0 olan değerleri alır
    data = cursor.fetchall() #sorgudan dönen değerleri atamak
    print("*******Değerleri 2.0 olan Veriler")
    for i in data:
        print(i)

def silveguncelle():
    cursor.execute("SELECT  * FROM Tablo3")
    data = cursor.fetchall()  # sorgudan dönen değerleri atamak
    print("*********İlk Değerler**************")
    for i in data:
        print(i)
    cursor.execute("UPDATE Tablo3 SET deger=99 WHERE deger=2.0")  #Değerleri güncellemek için kullanılan fonksiyon.


    cursor.execute("SELECT  * FROM Tablo3")
    data = cursor.fetchall()  # sorgudan dönen değerleri atamak
    print("*********GÜNCELLENEN Değerler**************")
    for i in data:
        print(i)

degerlerial()
silveguncelle()
con.close()