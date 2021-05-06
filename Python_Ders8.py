# Kök hesaplama Programı

#ax^2+bx+c

def kokbul(a,b,c):
    delta=b*b-4*a*c
    if delta<0:
        print("Reel kök yoktur!")
        return
    x1 = (-b - delta ** 0.5) / 2 * a
    x2 = (-b + delta ** 0.5) / 2 * a
    print("1.kök:",x1)
    print("2.kök:",x2)
    return(x1,x2)
i=1
while i<=3:
    i+=1
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))

    sonuc = kokbul(a,b,c)
    print(sonuc)




