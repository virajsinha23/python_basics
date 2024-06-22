#list
a= [34, 'people', 54, 'animals']
print(a)
print(type(a))
print(a[2])
print(a[1:3])
print(a*4)
print(len(a))
print(a[::-1])
a.append(40)
print(a)
a.remove('people')
a.remove('animals')
print(a)
#a.clear()
#print(a)
print(max(a))
print(min(a))

#tuple
b= (20,30,20,40,30,"human")
print(b)
print(type(b))
#b[2]= 100 # is immutable
#print(b)
print(b.index('human'))

#set
c= {30, 50, 30, 'chennai', 79}
print(c)
print(type(c))
c.update([60])
print(c)
c.remove('chennai')
print(c)
#frozen set does not allow update/allow anymore
#e=frozenset(c)
#e.update([20])

#dictionary
d= {1:'chennai', 2:'kolkata', 3:'pune'}
print(d)
print(type(d))
print(d.items())
k=d.keys()#displays all the keys
for i in k:print(i)
v=d.values()
for i in v:print(i) # displays all values
print(d[2])
del dict[2]
print(d)



