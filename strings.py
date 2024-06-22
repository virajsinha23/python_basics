#string creation
a= 'This is Python '
print(a)

#multi line
b= """this
is multi
line"""
print(b)

#index
print(b[6])

# * operation on a string
print (a*2)

#length of a string
print(len(b))

#slicing
print(a[0:3]) #write starting index:ending index
print(a[0:])
print(a[:8])
print(a[-5:-1])

#stepping in slicing
print(a[0::2])
print(a[::-1]) #reverse the string

#case of string
print(a.upper())
print(a.lower())
