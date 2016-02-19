"""
Python script set as part of our Computer Science course.

Manages a parcel delivery agency.
"""


class Parcel(object):
    """A parcel with dimensions and weight."""

    def __init__(self, length, width, height, weight):
        """Init."""
        super().__init__()
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.reject = False
        self.sum_dimensions = length + width + height

    def check(self):
        """Check the parcel's dimensions and weight."""
        if self.length > 80:
            print("Parcel too long.")
            self.reject = True
        if self.width > 80:
            print("Parcel too wide.")
            self.reject = True
        if self.height > 80:
            print("Parcel too high.")
            self.reject = True
        if self.sum_dimensions > 200:
            print("Parcel too large.")
            self.reject = True
        if self.weight < 1:
            print("Parcel too light.")
            self.reject = True
        if self.weight > 10:
            print("Parcel too heavy.")
            self.reject = True
        if self.reject:
            print("Parcel rejected.")
        else:
            print("Parcel accepted.")


def inp_parcel():
    """Ask the user to input a parcel's data."""
    while True:
        try:
            inp_length = float(input("Enter the parcel's length: "))
            inp_width = float(input("Enter the parcel's width: "))
            inp_height = float(input("Enter the parcel's height: "))
            inp_weight = float(input("Enter the parcel's weight: "))
            break
        except ValueError:
            print("\nERROR: Please enter proper numbers, e.g.: '45.55'.")
            print()
    global new_parcel
    return Parcel(inp_length, inp_width, inp_height, inp_weight)


def menu():
    """Display a menu for the user to select an option."""
    print("\nSelect an option:")
    print("\n\tA. Check a single parcel")
    print("\tB. Make a consignment")
    print("\tX. Exit")
    option = input("\nEnter your option: ").upper()
    if option == "A":
        print()
        optionA()
    elif option == "B":
        optionB()
    elif option == "X":
        exit()
    else:
        print("\nERROR: Please enter a proper option, e.g.: 'A'.")
    menu()


def optionA():
    """Check a parcel's dimensions and weight."""
    new_parcel = inp_parcel()
    print()
    new_parcel.check()


def optionB():
    """Check a customer's consignment of parcels."""
    consignment = []
    total_accepted = 0
    total_rejected = 0
    total_weight = 0
    while True:
        try:
            num_parcels = int(input("\nEnter the number of parcels \
in the consignment: "))
            break
        except ValueError:
            print("\nERROR: Please enter an integer, e.g.: '5'.")
    for i in range(num_parcels):
        print("\nEnter parcel #%s's information:" % i + 1)
        consignment.append(inp_parcel())
        consignment[i].check()
        if consignment[i].reject:
            total_rejected += 1
        else:
            total_accepted += 1
            total_weight += consignment[i].weight
    print("\nNumber of parcels accepted:", total_accepted)
    print("Total weight of parcels accepted:", total_weight)
    print("Number of parcels rejected:", total_rejected)

menu()
