# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

n=int(input())
x=list(map(int,input().split()))
f= list(map(int,input().split()))

S=[]
#S=[0]*5

for i in range(0, len(x)):
    t=0
    while t< f[i]:
        a=x[i]
        S.append(a)
        t=t+1
    

#print(S)
l=len(S)
#print(l)
q1=[]
q3=[]
#q2=[]
S.sort()

if l%2==0:
    a1= int(l/2)
    q1=S[0:a1]
    q3=S[a1:]
 #   print(q1)
 #   print(len(q1))
 #   print(q3)
 #   print(len(q1))
    q1.sort()
    q3.sort()
    Q1= median(q1)
    Q3= median(q3)
    
if l%2!=0:
    b1=l//2
    q1=S[0:b1]
    q3=S[b1+1:]
 #   print(q1)
 #   print(q3)
    q1.sort()
    q3.sort()
    Q1= median(q1)
    Q3= median(q3)
    
ir = round(float(Q3-Q1), 1)
print(ir)

