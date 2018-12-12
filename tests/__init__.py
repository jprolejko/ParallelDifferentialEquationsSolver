import unittest
import solver.equations_parser as parser


class TestEquationsParser(unittest.TestCase):

    def test_wrong_attribs(self):
        with self.assertRaises(AttributeError):
            equations = ['5', '2']
            initial_values = [0]
            interval = [0, 1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()
        with self.assertRaises(AttributeError):
            equations = ['x1 + 5', 'x1/x0']
            initial_values = [0, 2, 5]
            interval = [0, 1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()
        with self.assertRaises(AttributeError):
            equations = ['x2*x2 - x1', 'x1', '5*x2']
            initial_values = []
            interval = [0, 1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()

        with self.assertRaises(AttributeError):
            equations = ['x2 + 5*x1*(x0-x2) + (5*12) / x1', 'x0/(x1*x2) - (23/12) * x0', 'x1/x2*x0+x1 - x2']
            initial_values = [1, 1.2, 43.1]
            interval = [0]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()
        with self.assertRaises(AttributeError):
            equations = ['x2 + 5*x1*(x0-x2) + (5*12) / x1', 'x0/(x1*x2) - (23/12) * x0', 'x1/x2*x0+x1 - x2']
            initial_values = [1, 1.2, 43.1]
            interval = [0, -1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            equations = ['x3 + x2 - x0*12', 'x1/x2']
            initial_values = [0, 1]
            interval = [0, 1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            equations = ['x1/x0', '5']
            initial_values = [0, 1]
            interval = [0, 1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()

    def test_wrong_syntax(self):
        with self.assertRaises(SyntaxError):
            equations = ['x1/-=x0', '5']
            initial_values = [1, 1]
            interval = [0, 1]
            eq_parser = parser.EquationsParser(equations, initial_values, interval)
            eq_parser.parse()

    def test_right_syntax(self):
        equations = ['x2 + 5*x1*(x0-x2) + (5*12) / x1', 'x0/(x1*x2) - (23/12) * x0', 'x1/x2*x0+x1 - x2']
        initial_values = [1, 1.2, 43.1]
        interval = [0, 1]
        eq_parser = parser.EquationsParser(equations, initial_values, interval)
        test_case = True
        try:
            eq_parser.parse()
        except BaseException:
            test_case = False

        self.assertTrue(test_case)

        equations = ['x0', 'sin(t)']
        initial_values = [1, 1.2]
        interval = [0, 1]
        eq_parser = parser.EquationsParser(equations, initial_values, interval)
        test_case = True
        try:
            eq_parser.parse()
        except BaseException:
            test_case = False

        self.assertTrue(test_case)


if __name__ == '__main__':
    unittest.main()
