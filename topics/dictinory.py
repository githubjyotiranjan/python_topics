#unorder(dictionary), element can access by index are called order(list)

dictinary = {'name':'abc', 'age':30, 'location':'India', 'state':'Orissa'}
print(dictinary)
print(dictinary.keys())
# print(dictinary.has_key('location'))//works below python 3
print('location' in dictinary) #for key
print('location' in dictinary.keys())

print(dictinary.__contains__('location'))
# print('India' in dictinary) #not for value

print(dictinary.values())
print(type(dictinary.values()))
print('India' in dictinary.values())
print('location' in dictinary.keys())

# print(dictinary[0]) // error

# li = [1,2,3,4,5,6]
# print(6 in li)
#
# print(dictinary.__contains__('location'))

# In python3, has_key(key) is replaced by __contains__(key)

Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

