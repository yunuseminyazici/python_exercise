"""Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan
üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa,
ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak.
Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

abs(-4)
4
abs(5)
5
"""
print("1-----Üçgen için -------")
print("2-----Dörtgen için -------")

cevap=int(input("Üçgen mi Dörtgen mi? Lütfen Seçiniz="))

if cevap == 1:
    print("Lütfen 3 tane kenar uzunluğunu cm cinsinden giriniz")
    a = int(input("1. Kenar:"))
    b = int(input("2. Kenar:"))
    c = int(input("3. Kenar:"))

    if (abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if(a == b and a == c):
            print("Eşkenar Üçgen")
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkiz Kenar Üçgen")
        else:
            print("Çesit Kenar Üçgen")

elif cevap==2:
    print("Lütfen 4 tane kenar uzunluğunu cm cinsinden giriniz")
    d = int(input("1. Kenar:"))
    e = int(input("2. Kenar:"))
    f = int(input("3. Kenar:"))
    g = int(input("4. Kenar:"))

    if  d==e and d==f and d==g:
        print("Kare")
    elif d==f and e==g:
        print("Dikdörtgen")
    else:
        print("Dikdörtgen")




