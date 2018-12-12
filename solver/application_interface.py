class ApplicationInterface:

    def __init__(self):
        self.number_of_equations = 0
        self.equations = []
        self.step = 0
        self.interval = [0, 0]
        self.initial_conditions = []

    def init_equations(self):
        print("Parallel Differential Equations Solver")
        print("")
        print("Functions are x0, x1, ..., xn - where n is number of all functions and number of equations.")
        print("Each function is a variable of t - time.")
        print("Every equation should be first order and decoupled.")

        while True:
            try:
                self.equations.clear()
                self.initial_conditions.clear()

                self.number_of_equations = int(input("Enter number of equations: "))

                for index in range(0, self.number_of_equations):
                    self.equations.append(input("Equation no. " + str(index) + ": dx" + str(index) + "/dt = "))

                print("System of loaded equations presented below: ")

                for index, equation in enumerate(self.equations):
                    print("dx" + str(index) + "/dt = " + equation)

                self.step = float(input("Enter step of integration: "))

                if self.step <= 0:
                    raise ValueError("step of integration")

                interval = input("Enter interval of integration in template <t0, t1>: ")

                interval = interval.split(',')

                self.interval[0] = int(interval[0][1:])
                self.interval[1] = int(interval[1][:-1])

                if self.interval[0] > self.interval[1]:
                    raise ValueError("interval")

                for index in range(0, self.number_of_equations):
                    self.initial_conditions.append(int(input("Enter initial condition of x" + str(index) + " = ")))

                break

            except ValueError:
                print("Wrong syntax!")
            except IndexError:
                print("You need to enter two bounds of interval separated by coma!")

    @staticmethod
    def computation_succeeded():
        print("Solving passed!")
        print("Computation results have been printed to results.csv file.")

    @staticmethod
    def computation_failed():
        print("Solving failed!")
        print("Most likely, there were some mistakes in equations definitions.")

    def return_equations(self):
        return self.equations

    def return_step(self):
        return self.step

    def return_initial_conditions(self):
        return self.initial_conditions


if __name__ == '__main__':
    print("Cannot be executed standalone. Some mistake occurred...")
