"""
i=0
while(i<10):
    print("i'nin değeri:",i)
    i+=1 #veya "i=i+1"

"""
defkullanici="yunus"
defsifre="3232"

while(True):
    kullanici=input("Kullanici Adiniz")
    parola=input("Parolanızı giriniz")

    if ((kullanici==defkullanici) and (defsifre==parola)):
        print("Hosgeldiniz")
        break

    elif ((kullanici!=defkullanici) and (defsifre==parola)):
        print("Yanlış Kullanici Adi")
    elif ((kullanici==defkullanici) and (defsifre!=parola)):
        print("Yanlış parola girdiniz")
        print("Sifreyi Değiştirmek ister misiniz? E/H")
        cevap=input()

        if (cevap=="E"):
            newpassword=input("Yeni Şifrenizi Giriniz:")
            defsifre=newpassword
            print("Sifreniz Basarı ile değiştirildi")
        else:
            continue




