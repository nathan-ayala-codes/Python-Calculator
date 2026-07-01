import sys
class Calculator:
    def __init__(self) -> None:
        self.num1 = None
        self.num2 = None
        self.output = None

    def addition (self) -> None:
        self.output = self.num1 + self.num2
        print(f"Answer = {self.output}")

    def subtraction(self) -> None:
        self.output = self.num1 - self.num2
        print(f"Answer = {self.output}")

    def multiplication(self) -> None:
        self.output = self.num1 * self.num2
        print(f"Answer = {self.output}")

    def division(self) -> None:
        try:
            self.output = self.num1 / self.num2
            print(f"Answer = {self.output}")
        except ZeroDivisionError:
            print("Cannot divide by zero, try again")

class MenuControl:
    def __init__(self):
        self.C1: Calculator = Calculator()
    def homeMenu(self) -> None:
        print(f"Nathan's Calculator"
              f"\n(a) Start"
              f"\n(b) Quit")
        choice = input("Enter Choice:")
        if choice == "a" or choice == "A":
            self.inputTwoNum(self.C1)
        else:
            self.quitScreen()

    def menu(self, obj: Calculator) -> None:
        print(f"(a) Apply operation on previous output"
              f"\n(b) Clear"
              f"\n(c) Quit")
        choice = input("\nEnter Choice:")
        if choice == "a" or choice == "A":
            self.inputOneNum(self.C1)
        elif choice == "b" or choice == "B":
            self.inputTwoNum(self.C1)
        elif choice == "c" or choice == "C":
            self.quitScreen()
        else:
            print("Error Invalid Input")
            self.menu(self.C1)

    def inputTwoNum(self, obj: Calculator):
        try:
            obj.num1 = float(input("\nEnter the first number:"))
            obj.num2 = float(input("\nEnter the second number:"))
            self.operatorChoice(self.C1)
        except ValueError:
            print("Error enter a number.")
            self.inputTwoNum(self.C1)


    def inputOneNum(self, obj: Calculator):
        obj.num1 = obj.output
        obj.num2 = float(input("\nInput second number:"))
        self.operatorChoice(self.C1)
        self.menu(self.C1)

    def quitScreen(self):
        print("Thank you for using Nathan's Calculator!")
        print("See you Next time!")
        sys.exit()

    def operatorChoice(self, obj: Calculator) -> None:
        operator = input("\nEnter operator:")
        if operator == "+":
            obj.addition()
            self.menu(self.C1)
        elif operator == "-":
            obj.subtraction()
            self.menu(self.C1)
        elif operator == "*":
            obj.multiplication()
            self.menu(self.C1)
        elif operator == "/":
            obj.division()
            self.menu(self.C1)
        else:
            print("Invalid Operator, try +, -, *, /")
            self.operatorChoice(self.C1)