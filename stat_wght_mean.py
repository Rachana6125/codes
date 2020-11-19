n= int(input())
x=list(map(int, input().split()))
w=list(map(int, input().split()))
weights=[]

for i in range(n):
    wt=x[i]*w[i]
    weights.append(wt)

ans = sum(weights)/sum(w)

print("{:.1f}".format(ans))
