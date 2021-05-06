class dusman:
    kalan_can=3
    def saldir(self):
        print("***Düşman saldiriyor!!***")
        print("Hucum")
        self.kalan_can -=1
    def hayatta_mi(self):
        if(self.kalan_can <=0):
            print("Düşman Öldü!")
        else:
            print("Düşmanın kalan canı:" + str(self.kalan_can) )

dusman1=dusman()
dusman2=dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()

dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayatta_mi()

