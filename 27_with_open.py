#amra jani je ekta file open korle close korte hoy na korle onno keu sei file access korte pare na ba exta space khay. ...er poriborte jodi amara open with use kroi tahole ar close() function use korte hobe na eka eka off hoye jabe code execute howar pore. 
with open("secret_file.txt", "r") as file:
    data = file.read()
    print(data)