n=int(input())
while n>=1:
    i=str(input())
    m=len(i)
    e=""
    o=""
    for p in range(0, m, 2):
        e+=i[p]
    for p1 in range(1, m, 2):
        o+=i[p1]
    print(e, o)
    n-=1
