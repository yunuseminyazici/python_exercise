print("Oyuncu Kaydetme Programı")
adi=str(input("Oyuncunun adini giriniz:"))
soyadi=input("Oyuncunun Soyadini Giriniz:")
takim=input("Oyuncunun takimini giriniz:")


bilgiler=[adi,soyadi,takim]

print("Oyuncunun adi:{}\nOyuncunun Soyadi:{}\nOyuncunun Takimi:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

sayi1= int(input("1. sayiyi giriniz:"))
sayi2= int(input("2. Sayiyi giriniz:"))
sayi3= int(input("3. Sayiyi giriniz:"))

carpim= sayi3*sayi2*sayi1

print("{} * {} * {} = {}".format(sayi1,sayi2,sayi3,carpim))



