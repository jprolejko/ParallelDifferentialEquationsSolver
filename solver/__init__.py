import solver.application_interface as ui
import solver.equations_parser as parser
import solver.runge_kutta_method as rk4
from multiprocessing import Pool


def append_file(time, values):
    with open("results.txt", "a") as file:
        file.write(str('%.4f' % time) + ", " + str(values) + '\n')

    return True


def main():
    app_interface = ui.ApplicationInterface()
    app_interface.init_equations()

    eq_parser = parser.EquationsParser(app_interface.return_equations(),
                                       app_interface.return_initial_conditions(),
                                       app_interface.return_interval())

    try:
        pool = Pool()
        eq_parser.parse()
        app_interface.print_info('Parsing passed!')

        rk = rk4.RungeKuttaMethod(eq_parser.return_parsed())

        values = eq_parser.return_initial_values()
        time = app_interface.return_interval()[0]
        end = time

        with open("results.txt", "w") as file:
            file.write(str('%.4f' % time) + ", " + str(values) + '\n')

        while time - app_interface.return_step() <= app_interface.return_interval()[1]:
            result = pool.apply_async(append_file, [end, values])
            end, values = rk.compute(time, values, app_interface.return_step())
            time = end

            while not result.get():
                pass

    except IndexError:
        app_interface.print_error('Unknown variable used in equations!')
    except SyntaxError:
        app_interface.print_error('Wrong syntax of equations!')
    except ZeroDivisionError:
        app_interface.print_error('Given initial conditions cause zero division error!')


if __name__ == '__main__':
    main()
