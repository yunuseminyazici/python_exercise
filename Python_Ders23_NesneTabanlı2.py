class dusman():

    def __init__(self,isim="Dusman",kalan_can=100,saldiri_gucu=55,mermi_sayisi=20 ): #Mavi renkle yazılan değerler default değerlerdir eğer sadece dusman() fonks çağılırsa bu değerler gözükür
        self.isim= isim
        self.kalan_can= kalan_can
        self.saldiri_gucu= saldiri_gucu
        self.mermi_sayisi= mermi_sayisi

    def print(self):
        print("Düşman Kimliği Basılıyor ")
        print("Düşman İsmi:",self.isim,"\n","Kalan Can:",self.kalan_can,"\n","Saldiri Gücü:",self.saldiri_gucu,"\n","Mermi Sayisi:",self.mermi_sayisi)


dusman1= dusman("Yunus",100,200,35)
dusman2= dusman("Ali",75,150,55)
dusman3= dusman()

print("***Düşman 1***")
dusman1.print()
print("***Düşman 2***")
dusman2.print()
print("***Düşman 3***")
dusman3.print()

