import solver.config as config
from math import sin, cos, tan, sqrt, pow, log


class EquationsParser:

    def __init__(self, equations, initial_values, interval):
        self.equations = equations
        self.parsed_equations = []
        self.initial_values = initial_values
        self.interval = interval

    def parse(self):
        if len(self.initial_values) != len(self.equations):
            raise AttributeError("Initial values should be the same size as equations!")

        if len(self.interval) != 2:
            raise AttributeError("Wrong interval!")

        if self.interval[0] > self.interval[1]:
            raise AttributeError("Wrong interval!")

        globals()[config.FUNCTION_NAME] = self.initial_values
        globals()[config.VARIABLE_NAME] = self.interval[0]

        for equation_index, equation in enumerate(self.equations):
            variable_seen = False
            new_equation = ''

            for char in equation:
                if char == config.FUNCTION_NAME:
                    variable_seen = True
                    new_equation += char + '['
                    continue
                elif variable_seen and not char.isnumeric():
                    new_equation += ']'
                    variable_seen = False

                new_equation += char

            if variable_seen:
                new_equation += ']'

            equation = new_equation

            test_value = eval(equation)
            self.parsed_equations.append(equation)

    def return_parsed(self):
        return self.parsed_equations

    def return_initial_values(self):
        return self.initial_values

    def return_interval(self):
        return self.interval
