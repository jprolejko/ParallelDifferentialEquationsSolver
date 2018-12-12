class EquationsParser:
    FUNCTION_NAME = 'x'
    VARIABLE_NAME = 't'

    def __init__(self, equations, initial_values, interval):
        self.equations = equations
        self.initial_values = initial_values
        self.interval = interval

    def parse(self):
        if len(self.initial_values) != len(self.equations):
            raise AttributeError("Initial values should be the same size as equations!")

        if len(self.interval) != 2:
            raise AttributeError("Wrong interval!")

        if self.interval[0] > self.interval[1]:
            raise AttributeError("Wrong interval!")

        globals()[self.FUNCTION_NAME] = self.initial_values
        globals()[self.VARIABLE_NAME] = self.interval[0]

        for equation_index, equation in enumerate(self.equations):
            variable_seen = False
            new_equation = ''

            for char in equation:
                if char == self.FUNCTION_NAME:
                    variable_seen = True
                    new_equation += char + '['
                    continue
                elif variable_seen and not char.isnumeric():
                    new_equation += ']'
                    variable_seen = False
                elif char.isalpha() and (char != self.FUNCTION_NAME or char != self.VARIABLE_NAME):
                    raise SyntaxError

                new_equation += char

            if variable_seen:
                new_equation += ']'

            equation = new_equation

            test_value = eval(equation)

