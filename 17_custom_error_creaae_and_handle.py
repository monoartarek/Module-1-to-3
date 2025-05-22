def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("only .txt files are allowed")
    print("Valid File")

# check_file('data.png') 


# ei custom error ta handle korbo ekhon.create jehetu korlam ekhon to handle o korte hobe tyna.
try:
    check_file('data.png')
except Exception as e:
    print(e) #"raise" er moddhe ja likhchilam seita show korbe 


