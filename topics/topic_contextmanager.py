"""
 use for managing resoueces like file operation and database connection as they are limited in supply.
 need to make sure release resources after use, other wise lead to leakahe amy cause system slow or crash.
 most common way to handle resources is by using the with keyword.

"""

with open("topis_dict.txt") as f:
    data = f.read()

#likage may happen as toomany files are opened
file_descriptors = []
for x in range(10):
    file_descriptors.append(open('topis_dict.txt', 'w'))
    print(x)

# print(file_descriptors)
# Traceback (most recent call last):
#   File "topic_contextmanager.py", line 14, in <module>
# OSError: [Errno 24] Too many open files: 'topis_dict.txt'

"""
Creating a Context Manager :
when user creating content manager using calass, to method need to be present __enter__()and __exit__()
__enter__() returns resource that need to be managed.__exit__() doesnot return anything but performs clean up operation
"""

class FileManager:

     def __init__(self, filename, mode):
         print('init method called')
         self.filename = filename
         self.mode = mode
         self.file = None

     def __enter__(self):
         print('enter method')
         self.file = open(self.filename, self.mode)
         return self.file
     def __exit__(self, exc_type, exc_val, exc_tb):
         self.file.close()


with FileManager('topis_dict.txt', 'w') as f:
    f.write('Test')

print(f.closed)

# Python program shows the
# connection management
# for MongoDB
#
# from pymongo import MongoClient


class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

    # connecting with a localhost


with MongoDBConnectionManager('localhost', '27017') as mongo:
    collection = mongo.connection.SampleDb.test
    data = collection.find({'_id': 1})
    print(data.get('name'))

