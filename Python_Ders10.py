def topla(liste):
    if(len(liste))==0:
        return  0
    else:
        return liste[0] + topla(liste[1:])  #Recusion kullanımı fonksiyon kendini otomatik olarak çağırır.

    """ liste[1,2,3,4]
    
    1.return 1 + topla([2,3,4])
    2.return 2 + topla([3,4])
    3.return 3 + topla([4])
    4.return 4 + topla([])
    
    """

sayi=int(input("listenin eleman sayısını girin:"))

while True: #Sonsuz döngüye sokmak için kullanıldı.
#Veriyi kullanıcıdan almak için:
    girilenliste=[]
    for i in range(0,sayi,1):
        a = int(input("{}.sayiyi gir:".format(i + 1))) #{}'daki yere format()'ın içindeki değer sırasıyla gelir.
        girilenliste += [a]
        if sayi <= i:
            break

    print("Toplam:", topla(girilenliste))

#print("Toplam:",topla([1,2,3,4])) veriyi otomatik alma