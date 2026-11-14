import json

with open("products.json", "r") as f:
    mahsulotlar = json.load(f)

nom = input("Mahsulot nomi: ")
miqdor = int(input("Yangi miqdor: "))

for m in mahsulotlar:
    if m["nom"] == nom:
        m["miqdor"] = miqdor
        with open("products.json", "w") as f:
            json.dump(mahsulotlar, f, indent=4)
        print("Miqdor yangilandi.")
        break
else:
    print("Mahsulot topilmadi.")
