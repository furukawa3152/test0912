def tset0912(A:int, B:str):
    B=sorted(map(int,B.split()))
    jugde=B[0]
    for i in range(1,A):
        if B[i]>B[i-1]:
            jugde=B[i]
    return (jugde*jugde)



def test1():
    assert tset0912(3, "3 2 1") == 9
