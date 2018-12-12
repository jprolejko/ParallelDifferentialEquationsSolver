class ApplicationInterface:

    def __init__(self):
        self.number_of_equations = 0
        self.equations = []
        self.step = 0

    def print_init(self):
        print("Parallel Differential Equations Solver")
        self.number_of_equations = int(input("Enter number of equations: "))

        for index in range(1, self.number_of_equations + 1):
            self.equations.append(input("Equation no. " + str(index) + ": dx" + str(index) + "/dt = "))

        print("System of loaded equations presented below: ")

        for index, equation in enumerate(self.equations):
            print("dx" +  str(index + 1) + "/dt = " + equation)

        self.step = float(input("Enter step of integration: "))

    def return_equations(self):
        return self.equations

    def return_step(self):
        return self.step


if __name__ == '__main__':
    print("Cannot be executed standalone. Some mistake occurred...")
