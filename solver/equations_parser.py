class EquationsParser:
    VARIABLE_NAME = 'x'

    def __init__(self, equations):
        self.equations = equations

    def parse(self):
        x = []
        for equation in self.equations:
            x.append(1.0)

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
