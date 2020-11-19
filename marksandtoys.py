#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    toys=prices
    ans=0
    #for i in prices:
    #    if i<=k:
    #        toys.append(i)

    #print(toys)
    toys.sort()

    for j in toys:
        if j<=k:
            ans+=1
            k-=j
            print(k)
        else:
            break
    return ans

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
