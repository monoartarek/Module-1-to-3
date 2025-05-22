#function 2 proker hoy ----> a) user defined b) built in (already banano) like: print(), input() ,sum()


#built in function niye alochona 
# hello = print("hello")
# print(hello)

# user_name = input("Enter your name: ")
# print(f"Hello{user_name}")\

# mx =max({1,2,3})
# print(mx)

# ------------------

#built in funcion niye alochona 

#type 01: No input , no return 
def my_first_function(): #define function 
    a = 10
    b = 12
    print(a + b)

my_first_function()  #function call kora 

#type 02: Input thakbe but no return 

def add_two_numbers(a , b): # argument
    print(a + b)

add_two_numbers(5, 10) # parameters 
add_two_numbers(100, 200)

#type 03: input , return 
def multiply_two_nums(a, b):
    return a * b

result = multiply_two_nums(12 , 2) #function return korle ekta varable e store korte hoy then print korte hoy 
print(result)


#type 04: no input , but return 

def hello():
    return "hello"

greetings = hello()
print(greetings)