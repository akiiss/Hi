d = int(input())
h = int(d/30)
m = int((d%30)*2)
txt = "It is {} hours {} minutes."
print(txt.format(h,m))