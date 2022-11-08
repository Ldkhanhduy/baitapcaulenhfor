n=int(input("Nhap so le nguyen duong n:"))
p=1
if n%2==0 or n <0:
    print("n phai la so le nguyen duong")
else:
    for i in range(1,n+1,2):
        p*=i
    print("P=",p)