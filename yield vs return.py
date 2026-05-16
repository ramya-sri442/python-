# yield vs return

#yeild it allows the values
'''a,b=[int(x) for x in input ("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

#return terminates the loop

'''a,b=[int(x) for x in input ("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#example

'''def mygen():
    #return "python"
    #return "java"
    #return "DSA"
    return "python","java","dsa" # if u want to remove this format so u can use *
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"
print(*mygen())'''    

def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"

d=mygen()
print(next(d))
print(next(d))
print(next(d))

