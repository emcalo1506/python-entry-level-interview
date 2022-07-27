

def nickname(name):
    if not name.isalpha():
        print("The name must have only letters")
        return False

    if len(name) < 5:
        print("The name must have at least 5 letters")
        return False
    else:
        return True

def password(passwd):
    special_sym = ['$', '@', '#', '%', '+']
    val = True

    if len(passwd) < 6:
        print('password should have at least 6 characters')
        val = False

    if len(passwd) > 20:
        print('password should not be longer than 20 characters')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one number')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in special_sym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


def isadmin(admin):
    if admin.lower() == "y":
        valadmin = True
        isadmin = True
    elif admin.lower() == "n":
        valadmin = True
        isadmin = False
    else:
        isadmin = False
        valadmin = False
        print("Invalid value")
    return isadmin, valadmin



def NewPerson():
    people = []

    while True:
        aw = input("You want to register a user (r) or login (l) or exit (e)? ")
        valpsw = False
        valname = False
        valadmin = False

        if aw.lower() == "r":
            while not valname:
                name = input("please enter your username: ")
                valname = nickname(name.strip())

            while not valpsw:
                pwd = input("please enter your password: ")
                valpsw = password(pwd.strip())

            while not valadmin:
                admin = input("are you admin? yes(y) or no(n)?: ")
                admin, valadmin = isadmin(admin.strip())

            person = [name.strip(), pwd.strip(), admin]
            people.append(person)

        elif aw.lower() == "l":
            salida = input("please enter your username: ")
            pwdL = input("please enter your password: ")
            user_exists = False
            for s in people:
                if s[0] == salida and s[1] == pwdL:
                    user_exists = True
                    asw = input(
                        "You want to list the users or delete any user?(d), change you password?(p), or LogOut(o)?: ")
                    if asw.lower() == "d":
                        if s[2]:
                            print("list of users:", people)
                            res = input("Do you want to delete any of them? yes(y) or no(n)?: ")
                            if res.lower() == "y":
                                nom = input("type the name of the person you want to delete: ")
                                if nom != salida:
                                    for d in people:
                                        if d[0] == nom:
                                            people.remove(d)
                                            print(nom, "successfully removed !!!")
                                else:
                                    print("You can't remove yourself from the list")
                        else:
                            print("Only administrators can delete another user and see the list of users")

                    elif asw.lower() == "p":
                        valpwd = False
                        while not valpwd:
                            newpwd = input("enter your new password: ")
                            if newpwd == pwdL:
                                print("passwords can't be the same")
                            else:
                                valpwd = password(newpwd)
                        people.remove(s)
                        s[1] = newpwd
                        people.append(s)
                        print("password changed successfully !!!")

                    elif asw.lower() == "o":
                        break
                    else:
                        print("Invalid input")

            if not user_exists:
                print("Wrong username or password")

        elif aw.lower() == "e":
            exit()
        else:
            print("Option not valid")


def main():
    print("Program is starting")
    NewPerson()



if __name__ == "__main__":
    main()