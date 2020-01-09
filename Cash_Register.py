#Calculates the change in a transaction.
#Accepts a value in cents and returns the number and type of coins for the given number

#Continuously asks for input until invalid input is given
while True:

    #Get user input
    inputChange = input('Enter your change: ')

    try:
        #Converts input if possible
        change = int(inputChange)

        #Checks if input is a positive number
        if change == 0 :
          print('No change! ')

        elif change > -1:
            print('Your change is: ')

            if change // 100 > 0:
                print(change // 100, ' Dollar(s)')
                change %= 100

            if change // 25 > 0:
                print(change // 25, ' Quarter(s)')
                change %= 25

            if change // 10 > 0:
                print(change // 10, ' Dime(s)')
                change %= 10

            if change // 5 > 0:
                print(change // 5, ' Nickle(s)')
                change %= 5

            if change // 1 > 1:
                print(change // 1, ' Pennies')

            elif change // 1 > 0:
                print(change // 1, ' Penny')

            change %= 1

        else:
            print('Negative Number: ')

            print(inputChange)

            break

    except ValueError:
        print('Invalid Input: ')

        print(inputChange)