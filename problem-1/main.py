# geometricforms is a program that print info about figures
# geometricforms es un programa que imprime información sobre las figuras




# Boolean variable to allow while loop to continue
# Variable booleana para permitir que el bucle while continúe
continueLoop = True

#resumir
def summarize(clist, testNumber):
    fname = "summary" + str(testNumber)
    print()
    print("*** Creating output for test " + str(testNumber))
    print()
    outf = open(fname, "w")

    if len(figures_registry) > 0:
        for item in figures_registry:
            outf.write(item.to_str() + " ")
        outf.write("\n")
    else:
        outf.write("-\n")

    outf.close()




from math import pi

figures_registry = []


class Cube(object):
    def to_str(self) -> str:
        return "Cube: Volume:" + str(self.volume **3)
    def __init__(self, v: int):
        self.volume = v


class Circle(object):
    def to_str(self) -> str:
        return "Circle: Radius:" + str(self.radius) + " Area:" + str(pi * self.radius ** 2) + " Perimeter:" + str(
            2 * pi * self.radius)
    def __init__(self, r: int):
        self.radius = r

class Square(object):
    def __init__(self, s):
        self.side = s
    def to_str(self):
        return "Square: Radius:" + str(self.side) + " Area:" + str(self.side ** 2) + " Perimeter:" + str(self.side * 4)



def main():
    print("Hello!")

    # Formatting the input shape to allow the input of upper/lowercase as well as odd spacing
    # Formatear la forma de entrada para permitir la entrada de mayúsculas/minúsculas así como el espaciado impar
    def format_input(text_line):
        text_line = text_line.lower().strip()
        word_list = text_line.split()
        text_line = " ".join(word_list)
        return text_line


    testNumber = input("What is the test number? ")

    while continueLoop:
        # prompts user for the shape
        # solicita al usuario la forma
        shape = input(
            "What shape would you like to calculate the metrics of? Input \"c\" for  \"cube\", \"q\" for \"quit\", \"ci\" for \"circle\",  \"s\" for \"square\": "
        )
        shape = format_input(shape)
        if shape == "q":
            print("You have reached the end of your session.")
            if not figures_registry:
                print("You did not perform any calculations.")
            else:
                print("The figures inserted are:")
                for i in figures_registry:
                    print(i.to_str())

                break


        elif shape == "ci":
            a = int(input("what is the radio of the circle: "))
            ci = Circle(a)
            print(ci.to_str())
            figures_registry.append(ci)

        elif shape == "s":
            a = int(input("what is the length of the square: "))
            s= Square(a)
            print(s.to_str())
            figures_registry.append(s)

        elif shape == "c":
            a = int(input("what is the length of the cube: "))
            c = Cube(a)
            print(c.to_str())
            figures_registry.append(c)


        else:
            print("enter proper value")


if __name__ == "__main__":
    main()
