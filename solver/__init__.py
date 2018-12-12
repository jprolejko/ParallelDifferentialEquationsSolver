import solver.application_interface as ui
import solver.equations_parser as parser
import solver.runge_kutta_method as rk4


def main():
    app_interface = ui.ApplicationInterface()
    app_interface.init_equations()

    eq_parser = parser.EquationsParser(app_interface.return_equations(),
                                       app_interface.return_initial_conditions(),
                                       app_interface.return_interval())

    try:
        eq_parser.parse()
        app_interface.print_info('Parsing passed!')

        rk = rk4.RungeKuttaMethod(eq_parser.return_parsed())

        end, values = rk.compute(eq_parser.return_interval()[0],
                                 eq_parser.return_initial_values(),
                                 app_interface.return_step())

        for i in range(0, 10000):
            end, values = rk.compute(end, values, app_interface.return_step())
            print(str(end) + ": " + str(values))

    except IndexError:
        app_interface.print_error('Unknown variable used in equations!')
    except SyntaxError:
        app_interface.print_error('Wrong syntax of equations!')
    except ZeroDivisionError:
        app_interface.print_error('Given initial conditions cause zero division error!')


if __name__ == '__main__':
    main()
