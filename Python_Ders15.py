sayi1= input("Sayi1=")
sayi2= input("Sayi2=")

#Hata düzenleme
try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    cevap = sayi1 / sayi2
    cevap=int(cevap)
    print(cevap)

except ValueError:
    print("Lütfen 10'luk tabanda bir sayi giriniz")

except ZeroDivisionError:
    print("Bir sayi 0'a bölünemez")

""" 
try:
    dosya=open("yunusyazici.txt","r")
except IOError:
    print("Dosa Bulunamadı")
finally:                       #Dosyanın güenli bir şekilde kapanmasını sağlar ve gereksiz yer harcamaz.
    dosya.close()     
 """