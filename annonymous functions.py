#rite a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''


#annonymous functions are nameless functions and we use a keyword called as lambda to create annonymous function
#syntax
#a =lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#task

'''a=lambda x:x.upper()
x=input()
print(a(x))'''


'''a=lambda x:x.upper()
print(a("ramya"))'''


'''a=lambda x:x.title()
x=input()
print(a(x))'''


'''a=lambda x,y :x+y
x=input("first name")
y=input("last name")
print(a(x,y))'''


'''a,b=[x for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filters()
'''a=[10,20,30,9,7]
for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{}
'''a=[[],(),{},set()," ",None,6,3.4,False]
b=list(filter(None,a))
print(b)'''

#map-->each object from a collection and forms a new

'''a=[1,2,3,4,5,6]
b=[7,8,9,10,11,12]
c=list(map(max,a,b))
d=list(map(min,a,b))
print(c)
print(d)'''

'''a=input("")
b=input("")
print(a+b)'''

'''a,b=input("enter the values").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter the values").split(",")]
print(a+b)'''


'''a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=list(map(int,input("enter the values").split(",")))
print(a)'''

'''a=tuple(map(int,input("enter the values").split(",")))
print(a)'''

'''a=set(map(int,input("enter the values").split(",")))
print(a)'''

a=input("enter the key & values")
b=dict(i.split(":") for i in a.split(","))
print(b)


    



