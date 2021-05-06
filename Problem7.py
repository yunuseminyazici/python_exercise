""""Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın."""

a= int(input("Sayi giriniz:"))
b= int(input("Sayi giriniz:"))
c= int(input("Sayi giriniz:"))

if(a>b and a>c):
    print("En Büyük Sayi:",a)
elif(b>a and b>c):
    print("En Büyük Sayi:",b)
elif(c>a and c>b):
    print("En Büyük Sayi:",c)

