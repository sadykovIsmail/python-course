def verify_card_number(card_number):
    # Remove spaces and dashes
    cleaned = ""
    for char in card_number:
        if char.isdigit():
            cleaned += char

    total = 0
    reverse_digits = cleaned[::-1]

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])

        # Double every second digit (excluding the check digit)
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
