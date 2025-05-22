#scope --->definition: a region where a variable is accessible

x = 10  #here x is a global variable which is also modifyable into a function this is a power but value jodi ekta block ba fuction er moddhe change kori tahole sudhu oi function er moddei simaboddho thakbe bahire gelei abar global variable er je man se man e thakbe 

print(x)

def func():
    y = 29 #local variable -->which is only available into this function 
    print("y = ", y)
    print(x)

    x = 200 # eta ekta global variable ami chailei evabe eke modify korte pari but eta sudhu work korbe ei block ba ei funciton er moddhei bahire abar ager value i thakbe.
func()


