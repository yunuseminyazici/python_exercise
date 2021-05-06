"""
dosya=open("sapsucker2","r")

print(dosya.read()) #Bütün hepsini yazdırır.
print(dosya.readline()) #Satır satır yazdırır.
print(dosya.readlines()) #Liste şeklinde yazıdırır.


with open("sapsucker2","r") as dosya:  #Dosya okunduktan sonra kapanır. bellekde yer işgal etmez
    dosya.seek(8)
    print(dosya.read())

dosya.seek(10) #dosyanın en başından beri 10 birim ilerler
print(dosya.read()) #10 birim ilerledikten sonra kalan cümleyi yazar


with open("sapsucker2","a") as dosya:
    dosya.write("Yazar: Zulfu Livaneli") #textin içine veri eklemek için kullanılır.



with open("sapsucker2", "r+") as dosya:  #Hem yazmak hem de okumak için en başa veri ekleme!
    metin=(dosya.read())
    dosya.seek(0)
    metin="Yazar: Zulfu Livaneli"+"\n"+metin
    dosya.write(metin)


liste=[1,2,3,4,5]
liste.insert(1,15) #1. indexe 15 elemanını atar.
print(liste)

"""

with open("supsucker2","r+") as dosya:   #dosyanın indexine veri eklemek için.
    data = dosya.readlines()
    data.insert(1,"Yunus Emin Yazıcı\n")
    dosya.seek(0)
    dosya.writelines(data)

