#amra ekhane ekta jinis 2 vabe dekhbo ...frist e jeta dekhtichi eta te ami jsut 2 ta value pass korte parbo but ami jodi mutiple value pass krote chai tahole amare *args use korte hobe args use korte seta tuple hishebe input nae and sobgulo sum function er maddhome jog kore 
def addition(a, b):
        result = a + b
        return result
r = addition(4, 20)
print(r)
 
#now we are going to do this same works using *args (args er poriborte jekono word use kora jabe but star * dite hobe age )

def new_addition(*args):
        print(args)
        return sum(args)

r_new = new_addition(10, 12, 14 ,17)
print(r_new)

#ami jodi na jani je kotogulo value jog korte hobe tahole evabe korbo eta integer , string or any data types hoite pare  