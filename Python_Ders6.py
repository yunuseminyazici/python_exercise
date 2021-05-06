

faktoriyel=1

while True:
    sayi=int(input("Lütfen Negatif olmayan bir sayi giriniz:"))

    if sayi<=0:
        print("Lütfen Negatif olmayan bir sayi giriniz:")

    else:
        for i in range(1,sayi+1):
            faktoriyel = faktoriyel*i     #faktoriyel *=i

        print("Faktoriyel=",faktoriyel)
        break
