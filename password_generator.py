import random as r

print("Welcome to Password Generator")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4")

    else:
        small_letters = "abcdefghijklmnopqrstuvwxyz"
        capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "@#$%&!"

        password = ""

        password = password + r.choice(small_letters)
        password = password + r.choice(capital_letters)
        password = password + r.choice(numbers)
        password = password + r.choice(symbols)

        all_characters = small_letters + capital_letters + numbers + symbols

        for i in range(length - 4):
            password = password + r.choice(all_characters)

        password_list = list(password)

        r.shuffle(password_list)

        final_password = ""

        for character in password_list:
            final_password = final_password + character

        print("Your generated password is:", final_password)

except ValueError:
    print("Please enter a valid number")