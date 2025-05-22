import functools  #ei package ti reduce function er jonno call kora hoyeche

#lambda is an anonymous function ----> unnamed function 
#print use kora jay na only return korte pare 

def square(x):
    return x * x
print(square(5))

#using lambda arguments: expression 

square = lambda x : x * x   #lambda function decrease the size of a code 
print(square(4))

#ex : 02

add = lambda a, b: a+ b
print(add(1, 2))

#ex: 03
students = [('Rahim', 60), ('karim', 49), ('Fahim', 80)]

sorted_student = sorted(students, key = lambda x: x[1])

print(sorted_student)

#we need to know another three function :
# 1)  map() 
# 2)  filter()
# 3)  reduce()

#first of all: 1) map()
nums = [1,2,3,4]
#now we want to square all of the elements of the list
#sq_nums = list(map(square korte chacchi, kar upor apply korte chacchi))
# map traverse kore 
sq_nums = list(map(lambda x: x*x, nums))
print(sq_nums)

# 2) filter()  ---> filter or chakni er moto kaj kore or search kore ane 
even = list(filter(lambda x : x % 2 == 0, nums))
print(even)

# 3) reduce() ---> eta use korar jonno "functools" name ekta package import korte hoy sobar upore 

sum = functools.reduce(lambda x, y : x+y, nums)
print(sum)