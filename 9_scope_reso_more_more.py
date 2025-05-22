#Ekta rules ache jar nam : LEGB rule 
# l --> local 
# E --> Encolosing 
# G --> Global
# B --> Built in Scope ex:(print, sum, max, input etc)
n = "global_variable"

def outer():
    n = "enclosing_varable"
    def inner():
        global n   #if i want to change global variable permanently then we have to use "global" keyword and then variable name. eta ashole global variable ke update kore.

        # nonlocal n ---> ei keyword use korle enclosing variable change kora jabe. 
        n = "local_variable"
        print(n)
    inner()
    print(n) # "global" keyword er karone kintu global variable er value change hoye geleo enclosing change hoilo na because tar sei power nai. 
outer()
print(n) # nested function e "global" keyword use korar karone global varible change hoye gache. raja ar raja thaklo na. tobe "global" keyword kintu enclosing ke change korte parlo na. eta tar power nai. 


#summary: 
# global ----> global variable change korte pare , not enclosing 
# nonlocal --> enclosing change korte pare, not global ke 