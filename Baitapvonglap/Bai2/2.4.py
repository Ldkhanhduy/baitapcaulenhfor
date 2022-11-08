n=int(input("Nhap so chan nguyen duong n:"))
p=1
if n%2==1 or n <0:
    print("n phai la so chan nguyen duong")
else:
    for i in range(2,n+1,2):
        p*=i
    print("P=",p)