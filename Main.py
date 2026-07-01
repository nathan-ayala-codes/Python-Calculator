class Calculator:
    def __init__(self) -> None:
        self.num1 = None
        self.num2 = None
        self.output = None

    def addition (self) -> None:
        self.output = self.num1 + self.num2
        print(self.output)

    def subtraction(self) -> None:
        self.output = self.num1 - self.num2
        print(self.output)

    def multiplication(self) -> None:
        self.output = self.num1 * self.num2
        print(self.output)

    def division(self) -> None:
        self.output = self.num1 / self.num2
        print(self.output)

class MenuControl:
    def __init__(self):
        self.C1: Calculator = Calculator()
    def homeMenu(self) -> None:
        print(f"Nathan's Calculator"
              f"(a) Start"
              f"(b) Quit")
        choice = input("Enter Choice:")
        if choice == "a" or choice == "A":
            self.inputTwoNum(self.C1)
        else:
            self.quitScreen()

    def menu(self, obj: Calculator) -> None:
        print(f"(a) Apply operation on previous output"
              f"(b) Clear"
              f"(c) Quit")
        choice = input("Enter Choice:")
        if choice == "a" or choice == "A":
            ...
        elif choice == "b" or choice == "B":
            ...
        elif choice == "c" or choice == "C":
            ...
        else:
            ...

    def inputTwoNum(self, obj: Calculator):
        obj.num1 = float(input("Enter the first number:"))
        obj.num2 = float(input("Enter the second number:"))
        self.operatorChoice(self.C1)
        self.menu(self.C1)

    def inputOneNum(self, obj: Calculator):
        obj.num1 = obj.num2
        obj.num2 = input("Input second number:")
        self.operatorChoice(self.C1)
        self.menu(self.C1)

    def quitScreen(self):
        ...

    def operatorChoice(self, obj: Calculator) -> None:
        operator = input("Enter operator:")
        if operator == "+":
            obj.addition()
            self.menu()
        elif operator == "-":
            obj.subtraction()
            self.menu()
        elif operator == "*":
            obj.multiplication()
            self.menu()
        elif operator == "/":
            obj.division()
            self.menu()