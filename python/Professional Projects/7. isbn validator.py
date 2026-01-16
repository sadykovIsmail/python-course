import re

def validate_isbn(isbn, length):
    # check correct length
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[:-1]              # all digits except last one
    given_check_digit = isbn[-1].upper() # last digit (uppercase if 'x')

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')

    # Check comma presence
    if ',' not in user_input:
        print("Enter comma-separated values.")
        return

    values = user_input.split(',')
    if len(values) != 2:
        print("Enter comma-separated values.")
        return

    isbn = values[0].strip()
    length_str = values[1].strip()

    # Validate length input
    if not length_str.isdigit():
        print("Length must be a number.")
        return

    length = int(length_str)

    # Validate acceptable lengths
    if length not in (10, 13):
        print("Length should be 10 or 13.")
        return

    # Check for invalid characters (before calculating)
    if not re.fullmatch(r'[0-9Xx]+', isbn):
        print("Invalid character was found.")
        return

    # Finally, validate the ISBN
    validate_isbn(isbn, length)


# ❗ Comment this line for freeCodeCamp tests
# main()
