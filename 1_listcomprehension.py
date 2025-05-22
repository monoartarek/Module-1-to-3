roll = [12 ,1 ,23, 22,27, 26,16]

result = []

for i in roll:
    if i % 2 == 0:
        result.append(i)

print(result)

#-----now doing that using by list comprehension --------
# basic syntex :    [expression for item in iterable if condition]

new_result = [i for i in roll if i % 2 == 0]
print(new_result)

#list comprehension means multiple line code in one line mattro
# 2 line ei hoye jabe 

#example 02:
b = [1,2,3,4,5] #output erokom chaitechi je --> [1,4,3,16,5]

new_b = [i**2 if i % 2 == 0 else i  for i in b]
print(new_b)