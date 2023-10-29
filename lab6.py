
# Kriti Shah and Matthew Toro
def encoder(password): #Encoder function, returns encoded password
    x = []
    y = ''

    for i in range(0, len(password)):
        x.append(int(password[i])+3)

    for i in x:
        y += str(i)

    return y


def decoder(password):  # Encoder function, adding three
    decoded_password = ''

    for digit in password:  # all the digit in password

        if digit.isdigit():  # if the digits are a digit
            number = int(digit)  # the digit makes it into an integer = number
            decode = number - 3  # make the encode by adding three to the digits
            decoded_password += str(decode)  # turn each decoded digit to a string and add to the new password str

    return decoded_password  # return the new string

def main():
    condition = True

    while condition: #Loop function
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit') #Menu
        user_input = int(input('Please enter an option: '))

        if user_input == 1: #Encoder option
            password = input('Please enter your password to encode: ')
            encoded = encoder(password)
            print('Your password has been encoded and stored!')
            print()

        if user_input == 2: #Decoder
            print('The encoded password is ' + str(encoded) + ', and the original password is ' + str(decoder(encoded)) + '.')
            print()

        if user_input == 3: #Exit function
            exit()

if __name__ == '__main__': #Main
    main()


