#error handling er aro kichu janbo amra ekhane upgraded 
# with open("namenai.txt",'r') as f:
#     print(f.read())


try:
    with open("15_name.txt",'r') as f:
        print(f.read())

#ekhon ekta error occur korbo jake zero divition error bole
    print(10/0)  #infinity

    x = int("abc") #this is not possible to assign a sring into an integer 

    a = [1,3,5]
    print(a[100])

    b = abc

except ZeroDivisionError:
    print("Error : Division by Zero is not possible")  

except ValueError:
    print("Error: Value Error")

except IndexError:
    print("IndexError: invalid index")

except Exception as e: #is the error has no name
    print("some error occurred !!", e)

except FileNotFoundError:
    print("file Not found")

