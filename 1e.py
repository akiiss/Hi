k, n = map(int, input().split())
cnt = 1
if k > n:
    print(f"{1} {n}")
else:
    while k < n:   
        n -= k 
        cnt += 1
        if k < n:
            continue
        else:
            print(f"{cnt} {n}")
            break
