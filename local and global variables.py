#global & local variables


#first case of global variable
a=2
def check1():
    print("the inside of value is",a)
check1()
print("outside",a)



#second case
'''a=2
def check():
    a=5
    a=a**2
    print(a)
check()
print(a)'''

#third case of both gloabal and local variables

'''a=2
b=2
def check():
    a=5
    print("inside",a)
    a=10
    print("update",a+5)
    b=12
    print("add a+b",a+b)
check()
print("a value is",a)
print("bvalue is",b)'''

#Usage of global keyword

'''a=5
def first():
    global a
    print("the inside value is",a)
    a=10
    print("the inside value is",a)
    global b
    b=10
    print("the b value is",b)
first()
print("the outside value is",a)
print("the outside value is",b)'''

