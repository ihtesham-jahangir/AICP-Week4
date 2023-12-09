class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length * self.side_length

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print("Hexagon:")
        print("Area:", self.calcArea())
        print("Perimeter:", self.calcPeri())
        print("Sum of angles:", self.calcAngleSum())

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length * self.side_length

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("Square:")
        print("Area:", self.calcAreaSquare())
        print("Perimeter:", self.calcPeriSquare())

def main():
    cnic = input("Enter your CNIC: ")
    last_digit = int(cnic[-1])
    hexagon = Hexagon(last_digit)
    square = Square(last_digit + 1)

    while True:
        choice = input("Enter 1 for hexagon, 2 for square, any other key to exit: ")
        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display()
        else:
            break

if __name__ == "__main__":
    main()
