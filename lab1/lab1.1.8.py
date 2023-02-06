# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?

# setup
NUMBER_OF_DIGITS = 4
DUPLICATES_FOUND = "There is an equal digits in the number you entered"
DUPLICATES_NOT_FOUND = "There are no equal digits in the number you entered"
INVALID_INPUT = "Invalid input!"
ENTER_NUMBER = "Please enter four digit number:\n"
number_of_attempts = 3
equals_digits = False

while True:
    number = input(ENTER_NUMBER)

    # validation
    if number.isdigit() and len(number) == NUMBER_OF_DIGITS:

        # making array of digits
        number = int(number)
        digits = []
        for i in range(NUMBER_OF_DIGITS):
            digit = number % 10
            digits.append(digit)
            number = number // 10

        # checking for duplicates
        for i in range(NUMBER_OF_DIGITS):
            for j in range(i + 1, NUMBER_OF_DIGITS):
                if digits[i] == digits[j]:
                    equals_digits = True
                    break
            if equals_digits:
                break

        # printing result
        message = DUPLICATES_FOUND if equals_digits else DUPLICATES_NOT_FOUND
        print(message)
        break
    else:
        if number_of_attempts == 1:
            break
        print(INVALID_INPUT)
        number_of_attempts -= 1
