import random #Random kütüphanesi çağırılır
import sqlite3



class dusman():

    def __init__(self,isim="Dusman",kalan_can=100,saldiri_gucu=55,mermi_sayisi=20 ):
        self.isim= isim
        self.kalan_can= kalan_can
        self.saldiri_gucu= saldiri_gucu
        self.mermi_sayisi= mermi_sayisi

    def saldir(self):
        print(self.isim + " Saldırıyor!!")
        harcanan_mermi=random.randrange(1,10)
        print(str(harcanan_mermi)+" kadar mermi harcandı")
        self.mermi_sayisi -= harcanan_mermi

        return (harcanan_mermi,self.saldiri_gucu)

    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu ):
        print("Vuruldum")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermi_bitii_mi(self):
        if (self.mermi_sayisi <=0):
            print(self.isim + " Konuşuyor:Mermim bitii!")
            return True
        return False

    def hayatta_mi(self):
        if(self.kalan_can <=0):
            print(self.isim + "Öldü!")
        else:
            print(self.isim + " kalan canı:" + self.kalan_can)

    def print(self):
        print("Düşman Kimliği Basılıyor ")
        print("---Düşman İsmi:",self.isim,"\n","Kalan Can:",self.kalan_can,"\n","Saldiri Gücü:",self.saldiri_gucu,"\n","Mermi Sayisi:",self.mermi_sayisi)


try:
    dusmanlar_listesi = []
    i=0
    while i<10:
        rastgele_can=random.randrange(100,200)
        rastgele_saldiri_gucu= random.randrange(20,40)
        rastgele_mermi= random.randrange(10,30)
        yeni_dusman= dusman("Düşman" + str(i+1), rastgele_can,rastgele_saldiri_gucu,rastgele_mermi)
        dusmanlar_listesi.append(yeni_dusman)
        i += 1

    print("********Oyuna Hoşgeldiniz***********")
    secim = str(input("Düşman listesini görmek için 'g' tuşuna basınız:"))
    if (secim=="g"):
        for dusman in dusmanlar_listesi:
            dusman.print()

    i=0
    a=int(input("Kaç Round Oynamak istersiniz?:"))

    while (i<a):

        saldiran_düsman = random.randrange(0,10)
        savunan_düsman = random.randrange(0,10)

        dondurulen_deger = dusmanlar_listesi[saldiran_düsman].saldir() #Döndürülen değerler (harcanan_mermi,saldiri_gücü)
        dusmanlar_listesi[savunan_düsman].saldiriyaugra(dondurulen_deger[0],dondurulen_deger[1])
        print("ROUND BİTTİ!")

        i += 1

except ValueError:
    print("Lütfen Bir Geçerli Bir Değer Giriniz!")




