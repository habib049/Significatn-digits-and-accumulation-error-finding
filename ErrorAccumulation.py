class ErrorAccumulation:
    def __init__(self):
        self._equation = ""
        self._operations = ['+', '-', '/', '*', '^']
        self._min_dp = 0

    def set_equation(self, equation):
        self._equation = equation

    def calculate_errors(self):
        operations = list(set(self._equation) & set(self._operations))

        if ('+' in operations) or ('-' in operations):
            self._add_sub_errors()
        elif ('*' in operations) or ('/' in operations):
            self._mul_div_errors()
        elif '^' in operations:
            self._pow_root_errors()
        else:
            print("Equation not supported")

    def _add_sub_errors(self):
        numbers = re.split('[-+]', self._equation)
        self._min_dp = len(min(list(map(self._get_decimal, numbers)), key=len))
        z = eval(self._equation)
        e = list(map(self._calculate_e_value, numbers))
        ez = sum([abs(x) for x in e])

        print(f'The absolute error is {float(ez):.{self._min_dp}e}')
        print(f'The relative error is {float(ez / z):.{self._min_dp}e}')

        absolute_error = float("{:.{precision}f}".format(ez, precision=self._min_dp))

        print("Error bounds : {:.{precision}f}".format(
            z - absolute_error,
            precision=self._min_dp
        ) + " <= z <= {:.{precision}f}".format(
            z + absolute_error,
            precision=self._min_dp
        ))

    def _mul_div_errors(self):
        numbers = re.split('[*/]', self._equation)
        self._min_dp = len(min(list(map(self._get_decimal, numbers)), key=len))
        z = eval(self._equation)
        e = list(map(self._calculate_e_value, numbers))
        ez = sum([abs(x / float(y)) for x, y in zip(e, numbers)])

        print(f'The relative error is {float(ez):.{self._min_dp}e}')
        print(f'The absolute error is {float(ez * z):.{self._min_dp}e}')

        absolute_error = float("{:.{precision}f}".format((ez * z), precision=self._min_dp))

        print("Error bounds : {:.{precision}f}".format(
            z - absolute_error,
            precision=self._min_dp
        ) + " <= z <= {:.{precision}f}".format(
            z + absolute_error,
            precision=self._min_dp
        ))

    def _pow_root_errors(self):
        number, power = self._equation.split('^')
        if '.' in number:
            self._min_dp = len(number.split('.')[1])
        else:
            self._min_dp = 0
        z = eval(self._equation.replace('^', '**'))
        e = self._calculate_e_value(number)
        ez = abs(float(power)) * abs((float(e) / float(number)))

        print(f'The relative error is {float(ez):.{self._min_dp}e}')
        print(f'The absolute error is {float(ez * z):.{self._min_dp}e}')

        absolute_error = float("{:.{precision}f}".format((ez * z), precision=self._min_dp))

        print("Error bounds : {:.{precision}f}".format(
            z - absolute_error,
            precision=self._min_dp
        ) + " <= z <= {:.{precision}f}".format(
            z + absolute_error,
            precision=self._min_dp
        ))

    def _calculate_e_value(self, number):
        if '.' in number:
            decimal_part = number.split('.')[1]
            power = -1 * int(len(decimal_part))
            return 1 / 2 * (10 ** power)
        else:
            return 0

    def _get_decimal(self, number):
        if '.' in number:
            return number.split('.')[1]
        else:
            return 0
