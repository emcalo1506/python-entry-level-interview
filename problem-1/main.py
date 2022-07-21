# geometricforms is a program that print info about figures

# Lists for the volumes of each shape
cubeList = []
cubeVolumeList = []

# Boolean variable to allow while loop to continue
continueLoop = True


def summarize(clist, testNumber):
    fname = "summary" + str(testNumber)
    print()
    print("*** Creating output for test " + str(testNumber))
    print()
    outf = open(fname, "w")
    output_cube_list(clist, outf)

    if len(figures_registry) > 0:
        for item in figures_registry:
            outf.write(item.to_str() + " ")
        outf.write("\n")
    else:
        outf.write("-\n")

    outf.close()

def output_cube_list(lst, outfile):
    lngth = len(lst)
    counter = 0
    if lngth > 0:
        for item in lst:
            str = "%6.2f" % item
            outfile.write(f"{cubeList[counter]} {str} ")
        outfile.write("\n")
        counter += 1

    else:
        outfile.write("-\n")


# Calculates cube volume
def cube_volume(a):
    volume = pow(a, 3)
    # returns calculated value
    return volume


from math import pi

# A global figures registry
figures_registry = []


def add_figure(figure):
    figures_registry.append(figure)


class Circle(object):
    """
    The circle class.
    """

    def __init__(self, r: int):
        """
        :param int r:
        """
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def to_str(self) -> str:
        """
        Convert class to string
        :rtype: ConnectionListener
        :return:
        """
        print("")
        return "Circle: Radius:" + str(self.radius) + " Area:" + str(self.area()) + " Perimeter:" + str(
            self.perimeter())


class Square(object):
    """The square class."""

    def __init__(self, s):
        self.side = s

    def area(self):
        """Returns the area."""
        return self.side * self.side

    def perimeter(self):
        """Returns the perimeter"""
        return self.side + self.side + self.side + self.side

    def to_str(self):
        """Prints the square."""
        return "Square: Radius:" + str(self.side) + " Area:" + str(self.area()) + " Perimeter:" + str(self.perimeter())


def main():
    print("Hello!")

    # Formatting the input shape to allow the input of upper/lowercase as well as odd spacing
    def format_input(text_line):
        text_line = text_line.lower().strip()
        word_list = text_line.split()
        text_line = " ".join(word_list)
        return text_line

    # Prompts user for which test number
    testNumber = input("What is the test number? ")

    # The loop that continuously prompts user for shapes until a q is entered
    while continueLoop:
        # prompts user for the shape
        shape = input(
            "What shape would you like to calculate the metrics of? Input \"c\" for  \"cube\", \"q\" for \"quit\", \"ci\" for \"circle\",  \"s\" for \"square\": "
        )
        # formats the shape string
        shape = format_input(shape)
        # if they chose to quit
        if shape == "q":
            # sorts each list of volumes
            cubeVolumeList.sort()
            print("You have reached the end of your session.")
            # checks if arrays are empty so the program can tell user they didn't input anything
            if not cubeVolumeList and not figures_registry:
                print("You did not perform any calculations.")
            else:
                print("The figures inserted are:")
                if cubeVolumeList:
                    print("Cube: ", end="")
                    print(*cubeVolumeList, sep=", ")

                if figures_registry:
                    for i in figures_registry:
                        print(i.to_str())

                break

        # if they chose circle
        elif shape == "ci":
            # prompts user for dimensions
            a = int(input("what is the length of the circle: "))
            c = Circle(a)
            print(c.to_str())
            figures_registry.append(c)
        # if they chose square
        elif shape == "s":
            # prompts user for dimensions
            a = int(input("what is the length of the square: "))
            my_square = Square(a)
            print(my_square.to_str())
            figures_registry.append(my_square)
        # if they chose cube
        elif shape == "c":
            # prompts user for dimensions
            a = int(input("what is the length of the cube: "))
            # calculates the volume in python file volume and prints the calculated volume after
            c = cube_volume(a)
            print("The volume of a cube with length ", a, " is: ", c)
            # adds the volume to list of volumes
            cubeVolumeList.append(c)
            cubeList.append(c)

        # if no valid shape is entered, tells user to enter again
        else:
            print("enter proper value")


if __name__ == "__main__":
    main()
