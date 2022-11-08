n=int(input("n="))
p=1
if n<0: print("n phai la so nguyen duong")
else:
    for i in range(n):
        p*=(1/(i+1))
    print("P=",p)
