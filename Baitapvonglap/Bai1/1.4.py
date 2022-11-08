from math import log

s=0
n=int(input("n="))
if n<0:
    print("n phai la so nguyen duong")
else:
    for i in range(n):
        s+=log(i+1)
    print("s=",s)