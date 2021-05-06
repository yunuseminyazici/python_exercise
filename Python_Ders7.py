
#Fonksiyon Kullanımı

def faktoriyel(deger):
    faktoriyel=1

    for i in range(1,deger+1):
        faktoriyel*=i
    print("Faktoriyel",faktoriyel)

while True:  #Hesaplandıktan sonra sürekli çağırır.
    sayi=int(input("Faktoriyelini hesaplamak istediğiniz sayiyi giriniz:"))
    faktoriyel(sayi)
