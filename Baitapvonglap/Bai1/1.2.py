s=0
n=int(input("n="))
if n%2==0 or n <0:
    print("n phai la so duong le")
else:
    for i in range(1,n+1,2):
        s=s+i
    print("s=",s)