
# Kriti Shah and Matthew Toro
#
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
            print('The encoded password is ' + str(encoded) + ', and the original password is ' + str(decoded(encoded)) + '.')
            print()

        if user_input == 3: #Exit function
            exit()


def encoder(password): #Encoder function, returns encoded password
    x = []
    y = ''

    for i in range(0, len(password)):
        x.append(int(password[i])+3)

    for i in x:
        y += str(i)

    return y

def decoded(password): #Decoder function, inverse of encoder
    x = []
    y = ''

    for i in range(0, len(password)):
        x.append(int(password[i])-3)

    for i in x:
        y += str(i)

    return y


if __name__ == '__main__': #Main
    main()