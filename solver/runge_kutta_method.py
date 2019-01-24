import solver.config as config
from math import sin, cos, tan, sqrt, pow, log


class RungeKuttaMethod:

    def __init__(self, equations):
        self.equations = equations

    def compute(self, start, initial_conditions, step):
        globals()[config.FUNCTION_NAME] = initial_conditions
        globals()[config.VARIABLE_NAME] = start

        end_conditions = [0]*len(self.equations)
        end = start

        k1 = k2 = k3 = k4 = [0]*len(self.equations)

        for index, equation in enumerate(self.equations):
            k1[index] = (step * eval(equation))

        for index, equation in enumerate(self.equations):
            globals()[config.VARIABLE_NAME] = start + step/2.0

            conditions = initial_conditions

            for index_con, condition in enumerate(conditions):
                condition += k1[index_con] / 2.0

            globals()[config.FUNCTION_NAME] = conditions

            k2[index] = (step * eval(equation))

        for index, equation in enumerate(self.equations):
            globals()[config.VARIABLE_NAME] = start + step / 2.0

            conditions = initial_conditions

            for index_con, condition in enumerate(conditions):
                condition += k2[index_con] / 2.0

            globals()[config.FUNCTION_NAME] = conditions

            k3[index] = (step * eval(equation))

        for index, equation in enumerate(self.equations):
            globals()[config.VARIABLE_NAME] = start + step

            conditions = initial_conditions

            for index_con, condition in enumerate(conditions):
                condition += k3[index_con]

            globals()[config.FUNCTION_NAME] = conditions

            k4[index] = (step * eval(equation))

        for index, equation in enumerate(self.equations):
            k = 1.0 / 6.0 * (k1[index] + 2 * k2[index] + 2 * k3[index] + k4[index])
            end_conditions[index] = (initial_conditions[index] + k)

        end += step

        return end, end_conditions

