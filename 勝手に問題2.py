def apology(P: int, K: int, N: int):
    if P <= N:
        humiliation = (N + (N - P + 1)) * P / 2
    else:
        humiliation = (N + 1) * N / 2 + (P - N)
    if humiliation < P * K:
        return "sorry" * P
    else:
        return P * K



P = int(input())
K, N = map(int, input().split())
print(apology(P, K, N))
