# Make a program that receives an integer "n" calculates the sum of 1 to n, then shows the sum 
n = int(input())
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("Total: ", sum)

