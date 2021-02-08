list = []
n = input()
list = [int(val) for val in n.split(',')]
k = len(list)
cnt = 0
for i in range(k):
    for j in range(i+1, k):
        if list[i] == list[j]:
            cnt +=1
print(cnt)











"""
f={}
ans=0
for num in nums:
    if not num in f:
        f[num]=0
    f[num]+=1
        
    for num in f:
        n=f[num]
        ans+=(n*(n-1)//2)
            
return ans
"""