#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[5,6,7,8,9,10]
check(*b)
c={8,9,10,11,12}
check(*c)
d={"name":"pooja","city":"vij"}
check(*d)'''

'''def check1(*a):
    b=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in
        b=b+i
            print(b)
check1(1,2,3,"pooja")'''

'''def details(**a):
    print(a)
    print(type(a))
details()
d={"id":[10,20,30],"values":[30,40,50]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"id":[10,20,30],"names":["ramya","sri","milky"]}
details(**d)'''

#both * and ** usage
def final(*a,**b):
    d=1
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)

data=(2,3,4,5,6,7)
details={"id":[10,20,30],"names":["vishnu","milky","sweety"]}
final(*data)
final(**details)
   
        



        



