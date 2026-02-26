def verify_card_number(card_number):
    # Remove spaces and dashes
    cleaned = ""
    for char in card_number:
        if char.isdigit():
            cleaned += char

    total = 0
    reverse_digits = cleaned[::-1]  # Process from right to left per Luhn spec

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])

        # Double every second digit (positions 1, 3, 5... in 0-indexed reversed order)
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit -= 9  # Same as summing the two digits (e.g. 16 → 1+6 = 7 = 16-9)

        total += digit

    # A valid card number produces a total divisible by 10
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
