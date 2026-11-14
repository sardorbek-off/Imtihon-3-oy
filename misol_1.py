def matritsa_yigindisi(matritsa):
    return sum(sum(q) for q in matritsa)


matritsa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Yig'indi:", matritsa_yigindisi(matritsa))
