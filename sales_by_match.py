#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    
    uniq=[]

    for i in ar:
        if i not in uniq:
            uniq.append(i)

    counts=[]

    for k in uniq:
            c= ar.count(k)
            counts.append(c)
    print(counts)

    p=0

    for x in counts:
        p=p + x//2

    return p


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
