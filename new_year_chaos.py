#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(n,q):
    org_q=[]
    org_ind=[]
    for i in range(n):
        x=i
        org_q.append(x+1)
        org_ind.append(x)
    #print(org_q) 
    #print(org_ind)
    #print(q)
    
    bribes=0
    for i in range(n-1,-1,-1):
        if q[i]-(i+1)>2:  # i+1 ki jagah can write orq_q[i]
       # if q[i]-org_q[i>2]: 
            print ('Too chaotic')
            return
        
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                bribes+=1
            
    print(bribes)


    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(n, q)
