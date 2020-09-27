import time
import random
count=1
tscore=0
print("30秒間に何問正解できるかな？ENTERキーでスタート！")
input()
stime=time.time()
while True:
    a=random.randint(1,13)
    b=random.randint(1,13)
    c=random.randint(1,13)
    qtime=time.time()
    print(a,"+",b,"+",c,"=?")
    x=input()
    x=int(x)
    rtime=time.time()
    if rtime-stime>=30:
        print("TIME UP 終了～！",count-1,"問正解でした。SCORE:",int(tscore),"点")
        if count<4:
             print("もう少し頑張りましょう")
        elif count<13:
             print("まだまだですな")
        else:
             print("やりますな～！！")
        break
    elif not(a+b+c)==x:
        print("残念！！",count-1,"問正解でした。SCORE:",int(tscore),"点")
        if count<4:
             print("もう少し頑張りましょう")
        elif count<13:
             print("まだまだですな")
        else:
             print("やりますな～！！")
        break             
    else:
        print("正解！！",count,"問正解")
        score=(30-(rtime-qtime))*5
    count=count+1
    tscore=tscore+score

        


    
    
