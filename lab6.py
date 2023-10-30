# Kriti Shah and Matthew Toro

def encoder(password): #Encoder function, returns encoded password
    z = []
    j = ''
    #Returns j

    for i in range(len(password)):
        z.append(str(int(password[i])+3)) #Appends encoded character into the list

    for i in z:
        j += str(i) #Changes list into string

    return j #Returns encoded string


def decoder(password):  # Encoder function, adding three
    decoded_password = ''

    for digit in password:  # all the digit in password

        if digit.isdigit():  # if the digits are a digit
            number = int(digit)  # the digit makes it into an integer = number
            decode = number - 3  # make the encode by adding three to the digits
            decoded_password += str(decode)  # turn each decoded digit to a string and add to the new password str

    return decoded_password  # return the new string

def main():
    while True: #Loop function
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit') #Menu
        print()
        user_input = int(input('Please enter an option: '))

        if user_input == 1: #Encoder option
            password = input('Please enter your password to encode: ')
            encoded = encoder(password) #Encodes password
            print('Your password has been encoded and stored!')
            print()

        if user_input == 2: #Decoder option
            print('The encoded password is ' + str(encoded) + ', and the original password is ' + str(decoder(encoded)) + '.')
            print()

        if user_input == 3:
            exit() #Exits program

if __name__ == '__main__': #Main
    main()


