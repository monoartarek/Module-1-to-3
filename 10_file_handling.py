#ekta file ke open korar jonno ekta built in function ache "open()" function. ei file different way te open kora jay like read mode hoite pare abar write mode hoite pare 
file = open('10_1_file_handling.txt','r') #here "r" means reading mode. ami read korte chai.
x = file.read()
print( x )

#kono ekta file er kaj seshe seita close korte hoy 

file.close()

print("------------------------------------")
#evabe bar bar open kora and close kora onek jhamelar baper so amra arekta niyem follow korbo "with" namer ekta function diye 
with open ('10_1_file_handling.txt', 'r') as f: #file ta read kore f er moddhe rakhlam 
    y = f.read()
    print(y)