def nickname(name):
    long = len(name)  # Calcular la longitud del nomre de usuario
    y = name.isalnum()  # Calcula que la cadena contenga valores alfanuméricos

    if y == False:  # La cadena contiene valores no alfanuméricos
        print("The name must have only letters")

    if long < 5:
        print("The name must have  5 letters")

    if long > 5 and y == True:
        return True  # Verdadero si el tamaño es mayor a 5 y menor a 13

def password(passwd):
    SpecialSym = ['$', '@', '#', '%', '+']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

def newPerson():

    valpsw= False
    correct= False

    while correct == False:
        name = input("please enter your name: ")
        if nickname(name) == True:
           correct = True

    while  valpsw==False :
        pwd = input("please enter your password: ")
        if (password(pwd)):
            valpsw = True

    admin = input("are you admin? yes or no?:    ")

    if admin == "yes":
        isadmin = True
    else:
        isadmin = False

    person = {'name': name, 'pwd': pwd, 'isadmin': isadmin}
    return person

people = []
people.append(newPerson())
print(people)