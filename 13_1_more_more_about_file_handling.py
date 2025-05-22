#amra er ager code e dekhlam "os" package ke call kore amra file ekta ache kina khuje ber korlam now amra dekhbo onno ekta upay e ekta built in function ache etar jonno sejonno amader "pathlib" namer package define kroe nite hobe
import os
import pathlib

file_path = pathlib.Path('10_1_file_handling.txt') #here "Path" P capital na dile vul hobe error show korbe
if file_path.exists():
    print("file exists")

print(os.path.abspath('10_1_file_handling.txt'))
print(os.path.getsize('10_1_file_handling.txt')) #bytes

with open('10_1_file_handling.txt','r') as f:
    print(f.read(10))