'''a=input()
for i in range(1):
    print(type(a))
    print(len(a))
    print(dir())
    print(dir("_builtins_"))'''
#print() ,input(),len(),range(),type()

'''print(max(10,20,30,40,2,8))
print(min(10,20,0,9,8,20))
#print(sum(10,2))#it raises error

a=1,2,4,3
print(sum(a))'''

#print(dict(a))


'''a="codegnan"
b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,"pooja")
print(b)
b["c"]="python"
b["o"]="class"
print(b)'''

#eval()
'''while True:
    a=float(input("value"))
    b=float(input("value"))
    print(a+b)''' 
'''while True:
    a=eval(input("a value"))#it evalutes both values like float int str 
    b=eval(input("b value"))
    print(a+b)'''
#zip()

'''a=[10,20,30,40]
b=["ramya","milky","sri","sai","karthik"]
print(a+b)
c=list(zip(a,b))
print(c)
c=tuple(zip(a,b))
print(c)
c=dict(zip(a,b))
print(c)'''

#enumerates()

'''names=["geethika","budigi","damodar","sairam"]
for i in range(len(names)):
    #print(i)
    #print(i,names[i])
    b=list(enumerate(names))
    print(b)
    b=list(enumerate(names,100))
    print(b)'''

#ASCII
#chr(),ord()
'''print(chr(56))
print(ord("a"))
print(ord("b"))'''

for i in range(65,91):
    print(chr(i),end=" ")

s=input("")
for i in s:
    print(i,"-",ord(i))
    








    
