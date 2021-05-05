class SignificantDigits:
    def __init__(self):
        self._significant_digits = 0
        self._whole_part = 0
        self._decimal_part = 0

    def count_significant_digits(self, number):
        self._significant_digits = 0
        # check if number contains 10's power
        number = number.split('x')[0] if 'x' in number else number

        if '.' in number:
            self._whole_part, self._decimal_part = number.split('.')
            if int(self._whole_part) > 0:
                self._whole_part = self._whole_part.lstrip('0')
                self._significant_digits += len(self._whole_part) + len(self._decimal_part)
            else:
                self._decimal_part = self._decimal_part.lstrip('0')
                self._significant_digits += len(self._decimal_part)
        else:
            number = number.lstrip('0')  # leading zeros are not significant
            # Trailing zeros in a whole number with no decimal shown are NOT significant
            number = number.rstrip('0')
            self._significant_digits += len(number)  # all remaining are significant

        return self._significant_digits