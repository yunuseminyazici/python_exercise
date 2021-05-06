 class Calisan():
    def __init__(self,isim,maas,departman):
        print("****Çalışan Sınıfının Yapıcı Fonksiyonu****")
        self.isim = isim
        self.maas = maas
        self.departman= departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri gösteiliyor....")
        print("isim:",self.isim,"Maaş:",self.maas,"Departmanı:",self.departman)

    def maasazamyap(self,zam_miktarı):
        print("Maaşa zam yapılıyor.")
        self.maas += zam_miktarı

    def departmandegıstır(self,yeni_departman):
        print("Departman Değiştiriliyor.")
        self.departman = yeni_departman

class Yönetici(Calisan):  #Kaltım tanımlama

    def __init__(self,isim,maas,departman,kisi_sayisi): #overriding üstüne yazma
        print("----Yönetici sınıfının yapıcı fonksiyonu----")
        super().__init__(isim,maas,departman) #yönetici içindeki fonksiyonu çağırdı tekrar yazmamak için
        self.kisi_sayisi_= kisi_sayisi
        # self.bilgilerigoster()
        #super().bilgilerigoster()
    def bilgilerigoster(self):
        print("----Yönetici sınıfının bilgileri Gösteriliyor----")
        print("isim:",self.isim,"Maaş:",self.maas,"Departmanı:",self.departman,"Kişi sayısı:",self.kisi_sayisi_)

    def kisisayisiartir(self,arttır):
        print("kiş sayısı arttırlıyor:")
        self.kisi_sayisi_ += arttır


yonetici = Yönetici("Yunus Emin",3500,"Drive&Automation",35)
yonetici.bilgilerigoster()
yonetici.kisisayisiartir(5)
yonetici.bilgilerigoster()