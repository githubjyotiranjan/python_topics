'''

 As you know, a module can contain multiple objects, such as classes, functions, etc.
 A package can contain one or more relevant modules.
  Physically, a package is actually a folder containing one or more module files.

Module Search Path

When the import statement is encountered either in an interactive session or in a script:

    First, the Python interpreter tries to locate the module in current working directory.
    If not found, directories in the PYTHONPATH environment variable are searched.
    If still not found, it searches the installation default directory.

As the Python interpreter starts, it put all the above locations in a list returned by the sys.path attribute.
'''

from mypackage import power, average, SayHello, add
SayHello("World")
# x=power(3,2)
# print("power(3,2) : ", x)
print(add(5,9))