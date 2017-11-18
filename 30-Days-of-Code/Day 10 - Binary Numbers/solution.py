#!/bin/python3

import sys


n = int(input().strip())

k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
string=""
for j in k[::-1]:
    string=string+str(j)
x=(len(string))
t=0
c=0
for i in range(x):
    m=string[i]
    if int(m) ==1:
        t+=1
        if t>c:
            c=t
    else:
        t=0
print(c)

            
