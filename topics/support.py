def print_func( par ):
   print("Hello : ", par)
   return True

def add(a, b):
    c = a+b
    return c


if __name__ == '__main__':
    print_func( "abc" )

print(__name__)
print(type(__name__))