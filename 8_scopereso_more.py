#Ekta rules ache jar nam : LEGB rule 
# l --> local 
# E --> Encolosing 
# G --> Global
# B --> Built in Scope

n = "Global_variable" #this is a global variable ja sobar upore thake

def outer():
    n = "Enclosing_variable" #jokhon ekta nested function thakbe tokhon setar upore je variable thake take enclosing variable bole and oi function ke enclosing function bole
    def inner():
        n = "local_variable" #etake local variable bole
        print(n) #upore n onekgulo ache but pirnt korbe "local_varable" because n ager sobgulo ke override korbe 

    inner()
    print(n) #ekhon vetorer nested function er bahire eshe jokhon print kortechi tokhon amra ourput pabo "enclosing_variable" because eta ekhon oi block er bahire chole ashche.
    
outer()
print(n) #eta abar print korbe "global_variable" because eta sob scope er bahire chole ashche ar global is always super hero jotoi function er vetore niye giye take change kori na keno bahire eshe tare dak dile i mean call korle se ja tai thakbe "king is always a king" global variable is a king.
