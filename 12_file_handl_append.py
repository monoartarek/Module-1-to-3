

#but eta to sob remove kore dae. ami chai je ager gulo ja ache thakbe ar ekhane ja likhbo segulo giye joma hobe tahole ki kora jay.

#etar jonno je method use kora hoy setake "append" method bole. jar jonno "a" use korbo.
with open('10_1_file_handling.txt','a') as f:
    f.write("Hello world\n")
    f.write("I am writing in a file are you ready\n")
    f.write("THis is testing")

#jodi list e add korte chai
lines = ['\nI love python\n' , '\nI am new to python\n']
with open('10_1_file_handling.txt', 'a') as f:
    f.writelines(lines)