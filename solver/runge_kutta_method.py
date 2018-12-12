import solver.config as config
from math import sin, cos, tan, sqrt, pow, log


class RungeKuttaMethod:

    def __init__(self, equations):
        self.equations = equations

    def compute(self, start, initial_conditions, step):
        globals()[config.FUNCTION_NAME] = initial_conditions
        globals()[config.VARIABLE_NAME] = start

        end_conditions = []
        end = start

        k1 = k2 = k3 = k4 = []

        for equation in self.equations:
            k1.append(step * eval(equation))

        for equation in self.equations:
            globals()[config.VARIABLE_NAME] = start + step/2.0

            conditions = initial_conditions

            for index, condition in enumerate(conditions):
                condition += k1[index] / 2.0

            globals()[config.FUNCTION_NAME] = conditions

            k2.append(step * eval(equation))

        for equation in self.equations:
            globals()[config.VARIABLE_NAME] = start + step / 2.0

            conditions = initial_conditions

            for index, condition in enumerate(conditions):
                condition += k2[index] / 2.0

            globals()[config.FUNCTION_NAME] = conditions

            k3.append(step * eval(equation))

        for equation in self.equations:
            globals()[config.VARIABLE_NAME] = start + step

            conditions = initial_conditions

            for index, condition in enumerate(conditions):
                condition += k3[index]

            globals()[config.FUNCTION_NAME] = conditions

            k4.append(step * eval(equation))

        for index, equation in enumerate(self.equations):
            k = 1.0 / 6.0 * (k1[index] + 2 * k2[index] + 2 * k3[index] + k4[index])
            end_conditions.append(initial_conditions[index] + k)

        end += step

        return end, end_conditions

