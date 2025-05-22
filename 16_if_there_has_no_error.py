
try:
    with open("15_name.txt",'r') as f:
        print(f.read())

except FileNotFoundError:
    print("file Not found")

else: #jodi kono error na thake tahole "else" dile ta dekhiye dae
    print("code executed successfully")

finally: #error thakuk ar na thakuk eita print hobei 
    print ("error thakleo print hobe na thakleo print hobei ")

#jodi ami ekta website banay jekhane user kono ekta photo upload dibe but ami chaitechi se ekta nirdisto format e dik like(.txt) onno kono format e nibo na tahole ei poddhoti follow korte hobe.
#eta ekta manually exception create ba trigger korar way. ami nijei ekta exception create korlam or "custom" error create korlam
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("only .txt files are allowed")
    print("Valid File")

check_file('data.png') #user png upload dilo but ami chai .txt so ekhane value error dekhabe(only .txt files are allowed show korbe) jodi abar .txt file dei tahole valid dekhabe