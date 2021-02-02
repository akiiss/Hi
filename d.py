a = 4
b = 1
c = -3
i = 1
k = 0
cnt = 0
while i <= 5:
    m = a/b
    n = a/c
    b+=4
    c-=4
    k = m + n
    cnt +=k
    i+=1
print(cnt)