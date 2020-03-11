import random
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
(note this is case sensitive)
Credits for credits
+ for addition
- for subtraction
* for multiplication
/ for division
V for volume brute force
AT for area of triangle
AR for area of a rectangle
AZ for area of a trapazoid
''')

    if operation == '+':
      number_1 = int(input('Please enter the first number: '))
      number_2 = int(input('Please enter the second number: '))
      print('{} + {} = '.format(number_1, number_2))
      print(number_1 + number_2)

    elif operation == '-':
      number_1 = int(input('Please enter the first number: '))
      number_2 = int(input('Please enter the second number: '))
      print('{} - {} = '.format(number_1, number_2))
      print(number_1 - number_2)

    elif operation == '*':
      number_1 = int(input('Please enter the first number: '))
      number_2 = int(input('Please enter the second number: '))
      print('{} - {} = '.format(number_1, number_2))
      print(number_1 - number_2)
      print('{} * {} = '.format(number_1, number_2))
      print(number_1 * number_2)

    elif operation == '/':
      number_1 = int(input('Please enter the first number: '))
      number_2 = int(input('Please enter the second number: '))
      print('{} - {} = '.format(number_1, number_2))
      print(number_1 - number_2)
      print('{} / {} = '.format(number_1, number_2))
      print(number_1 / number_2)
    elif operation == 'V':

      print('note this is only using multipycation to get numbers from volume')
      bforce = int(input('number to brute force '))
      while True:
        var1 = random.randint(1,bforce)
        var2 = random.randint(1,bforce)
        var3 = random.randint(1,bforce)
        result = var1 * var2 * var3
        if result == bforce:
          print(str(var1) + ', ' + str(var2) + ', ' + str(var3))
    elif operation == 'AT':
      b = int(input('base '))
      h = int(input('hight '))
      print(h * b / 2)

    elif operation == 'AR':
      b = int(input('length '))
      h = int(input('width '))
      print(h * b)

    elif operation == 'AZ':
      ps = int(input('paralel side 1 '))
      ps2 = int(input('paralel side 2 '))
      h = int(input('hight '))
      ps = ps + ps2
      print(ps / 2 * h)

    elif operation == 'Credits':
      print("The School Calc by Julian O'grady")

      print('╔════╦╗───────────╔╗──────╔╗───╔╗')
      print('║╔╗╔╗║║───────────║║──────║║──╔╝╚╗')
      print('╚╝║║╚╣╚═╦══╗╔══╦══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗')
      print('──║║─║╔╗║║═╣║╔═╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝')
      print('──║║─║║║║║═╣║╚═╣╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║')
      print('──╚╝─╚╝╚╩══╝╚══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝')

    else:
      print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Bon weekend!')
    else:
        again()

calculate()