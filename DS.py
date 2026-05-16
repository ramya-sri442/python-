n=int(input("value"))
copy=n
sum=0
while n!=0:
    d=n%100
    n//=10
    
if n==d:
    print("armstrong")

else:
    print("not armstrong")
    
