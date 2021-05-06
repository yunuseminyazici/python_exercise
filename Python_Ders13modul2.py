import ders12modul #modul 1deki fonksiyonu modul 2'ye çağırır.

ders12modul.naber()
print(ders12modul.mutlak(-13))

from ders12modul import *  #2. Yöntem

naber()
print(mutlak(-45))

import math  # Hazır    Matematik kütüphanesini çağırma

print(math.factorial(5))