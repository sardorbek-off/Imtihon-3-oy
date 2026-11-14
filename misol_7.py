import csv

mahsulotlar = [["Olma", 8000, 12], ["Non", 4000, 20], ["Sut", 14000, 5]]

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow(["nom", "narx", "soni"])
    print("Ustun nomlari faylga yozildi.")

    writer.writerows(mahsulotlar)
    print("Mahsulotlar faylga qo'shildi.")
