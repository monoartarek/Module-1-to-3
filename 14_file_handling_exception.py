 #ami jodi age thekei bujhte pari je kono error ba exception ashte pare code run korar pore tahole seta onek annoying ekta baper ba dekhte kharap lagbe er poriborte jodi kono notification dewa jay user ke tahole eita dekhte sundor hoy ...ar eita kora jay try and exception er maddhome.

# syntex:

# try:
#     ---block of code----

# except name_of_the_error:
#     print("je notification show koraite chaitechi")


try: #error wala part ta rakhte hoy "try" er moddhe 
    with open("rahim.txt", 'r') as f:
        print(f.read())
except FileNotFoundError: #error er poriborte ja show koraite chaitechi seta rakhi except er moddhe 
    print("Ei name e kono file e nai bhai")

#jodi ei try except bolck use na kortam tahole error dekahito evabe:

#     with open("rahim.txt", 'r') as f:
#          ~~~~^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'rahim.txt'


#ar block use korar pore dekhai evabe : 
# Ei name e kono file e nai bhai