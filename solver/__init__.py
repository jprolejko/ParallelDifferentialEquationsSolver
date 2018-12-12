import solver.application_interface as ui
import solver.equations_parser as parser


def main():
    app_interface = ui.ApplicationInterface()
    app_interface.init_equations()

    eq_parser = parser.EquationsParser(app_interface.return_equations(), app_interface.return_initial_conditions())
    eq_parser.parse()


if __name__ == '__main__':
    main()
