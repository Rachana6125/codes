import numpy as np
from scipy import stats

n=int(input())
arr=list(map(int, input().split()))

print(np.mean(arr))
print(np.median(arr))
print(int(stats.mode(arr)[0]))
