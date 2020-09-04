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
    file.close()

with open("abc.txt", 'r') as file:
    print(file.n)





