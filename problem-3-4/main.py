
app_name = 'main'  # here for namespacing of urls.
import numpy as np


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
    valname= False
    valreg= False
    people = []

    while valreg == False:
        aw = input("You want to register a user (r) or login (l) or exit (exit), capital letters are not accepted")
        valpsw = False
        valname = False
        if aw == "r":
            while valname == False:
                name = input("please enter your name: ")
                if nickname(name):
                    valname = True

            while  valpsw == False:
                pwd = input("please enter your password: ")
                if (password(pwd)):
                    valpsw = True

            admin = input("are you admin? yes or no?:    ")

            if admin == "yes":
                isadmin = True
            else:
                isadmin = False
        elif aw == "l":
                salida = input("please enter a name: ")
                pwdL = input("please enter a password: ")
                for s in people:
                    if s.__contains__(salida) and s.__contains__(pwdL):
                        asw= input ('You want to list or delete any user?(d), change you password?(p), or LogOut(o)')
                        if asw == "d":
                            if s.__contains__(True):
                                print("list of users:", people)
                                res= input("Do you want to delete any of them? yes(y) or no(n)")
                                if res == "y":
                                    nom = input("type the name of the person you want to delete")
                                    for d in people:
                                        if d.__contains__(nom):
                                            people.remove(d)
                                            print(nom, "successfully removed !!!")
                            else:
                                print("Only administrators can delete another user")

                        elif asw == "p":
                            newpwd=input("enter your new password")
                            if newpwd == pwdL:
                                print("passwords can't be the same")
                            else:
                                if (password(newpwd)):
                                    people.remove(s)
                                    s.remove(pwdL)
                                    s.add(newpwd)
                                    people.append(s)
                                    print("password changed successfully !!!")
                        elif asw == "o":
                                break

        elif aw == "exit":
            exit()

        person = {name, pwd, isadmin}
        people.append(person)
        valreg == True
    return

people = []
people.append(newPerson())
