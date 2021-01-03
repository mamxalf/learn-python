from geometry.triangle import count_wide as luas_segitiga
from geometry.square import count_wide as luas_persegi, info


def hitung_luas_persegi(sisi):
    return sisi * sisi


# print(hitung_luas_segitiga(3, 5))
print(luas_segitiga(3, 2))
# print(hitung_luas_persegi(5))
print(info('Luas'))
print(luas_persegi(4))
