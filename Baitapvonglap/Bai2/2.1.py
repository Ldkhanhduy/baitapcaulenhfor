p=1
n=int(input("n="))
if n<0: print("n phai la so nguyen duong")
else:
    for i in range(n):
        p*=(i+1)
    print("P=",p)