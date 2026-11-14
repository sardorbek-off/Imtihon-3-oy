mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

nom = input("Mahsulot nomi: ")
narx = int(input("Yangi narx: "))

if nom in mahsulotlar:
    mahsulotlar[nom] = narx
    print("Narx yangilandi.")
    print(mahsulotlar)
else:
    print("Mahsulot topilmadi.")
