"""Problem 5¶
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."""

a=int(input("Birinci sayi:"))
b=int(input("İkinci sayi:"))

print("birinci sayi:{}\nİkinci sayi:{}".format(a,b))

a,b=b,a

print("birinci sayi:{}\nİkinci sayi:{}".format(a,b))