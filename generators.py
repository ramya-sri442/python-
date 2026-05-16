#generator

#a=[exp foor variable in range]
'''a=[i for i in range(21)]
print(a)
print(type(a))'''

#generator
'''a=(i for i in range(21))
print(*a)
print(type(a))'''
#convert generator to list but it type is always generator

'''a=(i for i in range(21))
print(list(a))
print(type(a))'''

#convert generator to tupple but it type is always generator

'''a=(i for i in range(21))
print(tuple(a))
print(type(a))'''

#convert generator to set but it type is always generator
a=(i for i in range(21))
print(set(a))
print(type(a))
