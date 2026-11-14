def tahlil_qil(sonlar):
    juft = sum(x for x in sonlar if x % 2 == 0)
    toq = sum(x for x in sonlar if x % 2 != 0)
    eng_katta = max(sonlar)

    print("Juft sonlar yig'indisi:", juft)
    print("Toq sonlar yig'indisi:", toq)
    print("Eng katta son:", eng_katta)


sonlar = [12, 7, 5, 18, 9, 4]
tahlil_qil(sonlar)
