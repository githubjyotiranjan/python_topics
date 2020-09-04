# by Importing system we can get the expection error
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    # print("Hi...")
    # print(int(entry))
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
    except Exception as e:
        print("Oops!", e)
        print("Next entry.")
        print()
    finally:
        print("abbbc")
print("The reciprocal of", entry, "is", r)

"""
You can include an else clause when catching exceptions with a try statement. 
The statements inside the else block will be executed only if the code inside the try block doesn’t generate an exception.

"""

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')


