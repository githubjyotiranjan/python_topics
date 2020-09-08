
# a file named "geek", will be opened with the reading mode.
try:
    file = open('geek.txt', 'r')
    # This will print every line one by one in the file
    for each in file:
        print (each)
except Exception as e:
    print('system error', e)
else:
    print("geek.txt is in u r folder")
    # file.close()
print("Closed or not : ", file.closed)


with open("abc.txt", 'r') as filen:
    print(filen.name)
print("Closed or not : ", filen.closed)

 # file.closed Returns true if file is closed, false otherwise.
 # file.mode Returns access mode with which file was opened.
 # file.name Returns name of the file.
 # file.softspace



