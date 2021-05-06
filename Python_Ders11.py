"""

sozluk={"Phyton":"Güzel Bir Dil","Php":"Script Dili","Java":"Compile edilen bir dil"}

print(sozluk["Phyton"])

for i in sozluk.items(): #Sözlüğün içindeki elemanları yazdırır
   # print(i)
    print(i[0]+" "+i[1])

"""
dersler= {"Yunus":["Matematik","Fizik","Kimya"],"Ahmet":["Resim","Müzik"]}

print("Lütfen aşağıdaki isimlerden birini yazınız\n Yunus\n Ahmet")

isim=input("İsim Giriniz:")
print("{} nin aldığı dersler:".format(isim))
for i in (dersler[isim]):
    print(i)
