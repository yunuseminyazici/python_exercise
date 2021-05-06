#Kullanıcı adı ve Şifre oluştuma Karar verme

kullaniciadi="programcibebe"
sifre="3234"

kullanici=input("Kullanici Adınızı Giriniz:")
parola=input("Şifrenizi Giriniz")

if((kullaniciadi==kullanici) and (sifre==parola)):
    print("Giris Başarılı")
elif((kullaniciadi==kullanici) and (sifre!=parola)):
    print("Hatali şifre veya Kullanıcı Adı")
elif ((kullaniciadi != kullanici) and (sifre == parola)):
    print("Hatali giriş!")
else:
    print("Lütfen Tekrar Deneyiniz!!!")
