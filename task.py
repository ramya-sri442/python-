n=int(input("enter the no of students"))
a=0
b=0
for i in range(n):
    s=input(f"student{i}: ")
    if s=="present":
        a=a+1
       
    elif s=="absent":
        b=b+1
    else:
        print("invalid")
print("present students are:",a)
print("absent students are:",b)
print("total students are:",a+b)
    
    
        
    
