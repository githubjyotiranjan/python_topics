#pass by refernce behave tow types with mutable and immutable

def test(a, lis):
    lis=[1,2]
    lis.append(6)

    a=10
    c= a+2
    print(lis)
    return c

print(test(a=6, lis=[1,2,3]))