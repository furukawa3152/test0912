L,R=map(int,input().split())
N=int(input())
def fullbokko(L,R,N):
    L_punch = 0
    while True:
        if N % R == 0:
            break
        else:
            N-=L
            L_punch += 1
    return int(L_punch+N/R)
print(fullbokko(L,R,N))


