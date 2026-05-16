#list comprehension
'''a=["python","code","codegnan"]
b=str(a)
c=b.upper()
print(c)'''


#syntax
#a=[exp for var in collection/range]
'''b=["apple","ball"]
b=[i.upper() for i in b]
print(b)'''

#task
'''a=["vja","hyd","vzg"]
a=[i.title() for i in a]
print(a)'''


'''a=[1,2,3,4,5,6,8,12,13]
a=[i*i for i in a]
print(a)'''

#if usage in list comprehension

'''a=[i for i in range(21)if i%2==0]
print(a)'''

'''a=[i*i for i in range(16) if i%2==0]
print(a)'''

"""b=["apple","banana","grapes","mango","kiwi","dragon","berry"]
b=[i for i in b if "a" in i]
print(b)"""

#no elif usage in list comprehension

'''a=[i**2 if i%2==0 else i*5 for i in range(30) ]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range (5)]
print(c)


   
