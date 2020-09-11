#list comphrenshion
# List comprehension is an elegant way to define and create lists based on existinglists.


li = [1,2,3,4,5,6]
#[2,4,6,8,10,12]

li2 = []
for i in li:
   li2.append(i*2)
print(li2)
# print([1,2,3,4,5,6]*2)

lis2 = [i*2 for i in li]
print(lis2)
li_c = [ x*2 for x in range(1, 10)]
print(li_c)

#map itertes through each objects
my_pets = ['alfred', 'tabitha', 'william', 'arla']
# upper_li = [ str.upper(x) for x in my_pets ]
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

#filter  skips sequence based on condition  through each objects
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))
print(over_75)