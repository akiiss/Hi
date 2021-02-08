n = int(input())
i = 0
for i in range(n*10, 0, -1):
    if i%2==1 and i/10<n+1 and i/10<n:
        print(i, end=" ")

