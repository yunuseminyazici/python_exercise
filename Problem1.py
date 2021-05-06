"""Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın."""

sayi1= int(input("İlk sayıyı giriniz"))
sayi2= int(input("İkinci sayıyı giriniz"))
sayi3= int(input("Üçüncü sayıyı giriniz"))

carpim=sayi3*sayi2*sayi1

print("{}x{}x{}={}'dir".format(sayi1,sayi2,sayi3,carpim))

