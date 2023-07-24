lst=list(map(int,input().split()))
m=0
n=0
if len(lst)<2:
    print(lst[0])
if len(lst)==2:
    print(max(lst))
for i in range(0,len(lst)//2-1):
    if(len(lst)%2==0):
        m=lst[i]+lst[i+2]+m
        n=lst[i+1]+lst[i+3]+n
    if(len(lst)%2!=0):
        m=lst[i]+lst[i+2]+lst[i+4]+m
        n=lst[i+1]+lst[i+3]+n
print(m if m>n else n)
