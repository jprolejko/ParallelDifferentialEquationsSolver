import solver.application_interface as ui
import solver.equations_parser as parser


def main():
    app_interface = ui.ApplicationInterface()
    app_interface.init_equations()

    eq_parser = parser.EquationsParser(app_interface.return_equations(), app_interface.return_initial_conditions())

    try:
        eq_parser.parse()
        app_interface.print_info('Parsing passed!')
    except IndexError:
        app_interface.print_error('Unknown variable used in equations!')
    except SyntaxError:
        app_interface.print_error('Wrong syntax of equations!')
    except ZeroDivisionError:
        app_interface.print_error('Given initial conditions cause zero division error!')


if __name__ == '__main__':
    main()
