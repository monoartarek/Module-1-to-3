#ex: 01

def my_func(f_name, l_name, age):
    print(f"My name is {f_name} {l_name}. I am {age} years old")
    
my_func("Tarek", "Monoar", 23)
my_func(25, "Monoar", "Tarek")#evabe dile ultapalta hoye jay
my_func(age = 25, l_name = "Monoar", f_name = "Tarek")#evabe argument pass kora jay safest way te 

#egula **args akareo pass kora jay and value gulo dictionary format e save hoye thake and segulo call kora jay easy way te ete onekegulo data pass kroe subidhamoto call kora jay example:
print("-----------------------------------------------")

#ex: 02

def new_func(**data): 
    print(data) #dictionary akare value gulo day...key value format arki 
    print(f"my name is {data['f_name']} {data['l_name']}. I am {data['age']} years old.")

new_func(age = 44 , l_name = "Islam", f_name = "Shahidul", address = "Naogaon") #ekhane address kono kaje lagbe na but taw ami pass korte partechi eitai sudidha icche moto kaje lagano jabe jodi proyojon hoy.
