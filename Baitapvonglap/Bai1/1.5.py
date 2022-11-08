s=0
n=int(input("n="))
if n<0: print("n phai la so nguyen duong")
else:
    for i in range(n):
        s+=(1/(i+1))
    print("s=",s)