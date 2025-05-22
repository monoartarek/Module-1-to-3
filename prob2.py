#make a program that takes numbers until it finds zero. shows the result of multiplication of all the numbers taken.
print("Enter the no of cycle :",)
times = int(input())
mul = 1
while times > 0:
    print("Enter no which you want ot multiplied:")
    n = int(input())
    if n == 0:
        break
    else:
        mul *= n
    times -= 1

print("Total multiplication: ", mul)

