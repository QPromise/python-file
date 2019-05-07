print([(a,b,c) for c in range(1, 11) for b in range(1, c + 1) for a in range(1, b + 1) if a ** 2 + b ** 2 == c ** 2 and a + b + c == 24])

