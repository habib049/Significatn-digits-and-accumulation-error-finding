significant = SignificantDigits()

number=float(input("Enter number to find significant digits : "))

significant_digits = significant.count_significant_digits(number)
print(f'The significant digits in {number} : {significant_digits}')



print('\nFinding errors\n')
error_accumulation = ErrorAccumulation()
equation = input("Enter an equation : ")
error_accumulation.set_equation(equation)
error_accumulation.calculate_errors()
print('\n')
