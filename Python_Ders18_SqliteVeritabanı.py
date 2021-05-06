import sqlite3

con = sqlite3.connect("dersler.db")  #Database oluşturma
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT,numara INT,ogrencinotu INT)")  #tablo oluşturma ve veri tipi belirleme
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Yunus Emin','Yazici' ,1234,100)") #Değer eklemek için IN   SERT INTO fonks kullanılır
    con.commit()
    con.close()


tabloolustur()
degerekle()