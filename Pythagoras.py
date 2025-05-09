N = int(input())
for a in range(1,N):
    for b in range(1,N):
        for c in range(1,N):
            if a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2:
                print("a =", a, ",b =", b, " c =", c)