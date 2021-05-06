def kayit_ekle(ad="Bilgi yok",soyad="Bilgi yok",yas="Bilgi yok",meslek="Bilgi yok"):
    print("kayit ekleniyor")

    print("Adınız:{}\n Soyadınız:{}\n Yasınız:{}\n Mesleğiniz:{}\n".format(ad,soyad,yas,meslek))

    print("Kayit Basariyla Eklendi")

#Klavyeden alınan verileri fonksiyona yazdırır.

print("***Kullanıcı kaydetme programına hoş geldiniz***")

while True:  #Birden çok kullanıcı eklemek için döngü.

    a=str(input("ad:"))
    b=str(input("soyad:"))
    c=str(input("yas:"))
    d=str(input("meslek:"))

    ekle = kayit_ekle(a,b,c,d)
    print(ekle)



