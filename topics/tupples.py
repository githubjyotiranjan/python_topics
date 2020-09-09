# (ele) or ele1, ele2
# Immutable object (no add, edit, delite  only can access)

a = 'abc', 'India', 30
print(a[0])
# cli = list(a)
# print(list(cli))
# print(type(cli))
# li = [1,2,3,4,5,6]
# tli = tuple(li)
# print(tli)

# exit(0)

print(a)
print(type(a))  # tuple

b = 'abc'
print(type(b))  # str

c = 30
print(type(c))  # int

d = ("abc",)
print(type(d))

e, f, g = "abc", 30, 89
print(e)  # abc
print(type(e))  # string
print(f)  # 30
print(type(f))  # int

'''
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator
is paired together, and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

'''
li = [1, 2, 3, 4, 5, 6]
li2 = ['a','b','c','d','e','f']
#out put {1:'a',2:'b'}
new_li = zip(li,li2)
for i in new_li:
    print(i)

print(list(new_li))