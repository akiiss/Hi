k, n = map(int, input().split())
cnt = 1
if k > n:
    print(f"{1} {n}")
else:
    m = n/k+1
    h = n%k
    print(f"{m} {h}")
