s=0
n=int(input("n="))
if n%2==1 or n <0:
    print("n phai la so duong chan")
else:
    for i in range(2,n+1,2):
        s+=i
    print("s=",s)