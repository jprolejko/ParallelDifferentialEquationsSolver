class EquationsParser:
    VARIABLE_NAME = 'x'

    def __init__(self, equations, initial_values):
        self.equations = equations
        self.initial_values = initial_values

    def parse(self):
        if len(self.initial_values) != len(self.equations):
            raise AttributeError("Initial values should be the same size as equations!")

        x = self.initial_values

        for equation_index, equation in enumerate(self.equations):
            variable_seen = False
            new_equation = ''

            try:
                for char in equation:
                    if char == self.VARIABLE_NAME:
                        variable_seen = True
                        new_equation += char + '['
                        continue
                    elif variable_seen and not char.isnumeric():
                        new_equation += ']'
                        variable_seen = False
                    elif char.isalpha() and char != self.VARIABLE_NAME:
                        raise SyntaxError

                    new_equation += char

                if variable_seen:
                    new_equation += ']'

                equation = new_equation

                test_value = eval(equation)

            except IndexError:
                print("Equation no. " + str(equation_index) + " with unknown variable!")

            except SyntaxError:
                print("Wrong syntax in equation no. " + str(equation_index) + "!")

            except ZeroDivisionError:
                print("Division by zero in equation no. " + str(equation_index) + "!")
