#!/bin/python3

import sys


N = int(input().strip())

if N % 2 != 0:
    print("Weird")
elif 2<=N<=5:
    print("Not Weird")
elif N>20:
    print("Not Weird")
else:
    print("Weird")
