import unittest

import solver.equations_parser as parser


class TestEquationsParser(unittest.TestCase):

    def test_wrong_attribs(self):
        with self.assertRaises(AttributeError):
            equations = ['5', '2']
            initial_values = [0]
            eq_parser = parser.EquationsParser(equations, initial_values)
            eq_parser.parse()
        with self.assertRaises(AttributeError):
            equations = ['x1 + 5', 'x1/x0']
            initial_values = [0, 2, 5]
            eq_parser = parser.EquationsParser(equations, initial_values)
            eq_parser.parse()
        with self.assertRaises(AttributeError):
            equations = ['x2*x2 - x1', 'x1', '5*x2']
            initial_values = []
            eq_parser = parser.EquationsParser(equations, initial_values)
            eq_parser.parse()

    def test_out_of_bounds(self):
        equations = ['x3 + x2 - x0*12', 'x1/x2']
        initial_values = [0, 1]
        eq_parser = parser.EquationsParser(equations, initial_values)
        self.assertFalse(eq_parser.parse())

    def test_division_by_zero(self):
        equations = ['x1/x0', '5']
        initial_values = [0, 1]
        eq_parser = parser.EquationsParser(equations, initial_values)
        self.assertFalse(eq_parser.parse())

    def test_wrong_syntax(self):
        equations = ['x1/-x0', '5']
        initial_values = [0, 1]
        eq_parser = parser.EquationsParser(equations, initial_values)
        self.assertFalse(eq_parser.parse())

    def test_right_syntax(self):
        equations = ['x2 + 5*x1*(x0-x2) + (5*12) / x1', 'x0/(x1*x2) - (23/12) * x0', 'x1/x2*x0+x1 - x2']
        initial_values = [1, 1.2, 43.1]
        eq_parser = parser.EquationsParser(equations, initial_values)
        self.assertTrue(eq_parser.parse())


if __name__ == '__main__':
    unittest.main()
