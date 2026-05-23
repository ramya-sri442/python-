#regular expression(regax-->only string)
'''a="codegnan in vij"
print(a)'''

'''a="codegnan\nin\na\tvijayawaa"
print(a)'''



#rstring
'''a=r"codegnan\nis\tin\nvij"
print(a)'''



#compile(),search(),findall(),split(),sub()
#sequence characters

'''w---> it mathches alphanumeric
W---> it mathches non alpha-numeric
d---> it mathches any digit
D---> it mathches -non-digit
s--->it represents white spaces
S--->it represents non-white spaces'''

#compile()
import re
'''a="map math cat cash money cup cap mug codegnan"
b=re.compile(r"m\w\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall
'''b=re.findall("c\w+",a)
print(b)'''

#split()
'''a="map code mug codegnan"
a=re.split(r"m",a)
print(a)'''

#sub
'''a=re.sub(r"maths","science",a)
print(a)'''


import re
a="year 2026 month 5 date 22"
b=re.findall(r"\d+",a)
print(b)



