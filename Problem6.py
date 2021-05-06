"""Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez """

boy= float(input("Boyunuzu giriniz:"))
kilo= int(input("Kilonuzu giriniz:"))

bik=kilo/(boy**2)
print("beden kitle endeksiniz:",bik)

if(bik<18.5):
    input("Zayıf")
elif(18.5<=bik<25):
    input("Normal")
elif(25<=bik<30):
    input("Fazla Kilolu")
elif(bik>30):
    input("Obez")
