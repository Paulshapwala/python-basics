def subtract(a, b):
    ans = a - b
    return ans


def multiply(a, b):
    ans = a * b
    return ans


def divide(a, b):
    ans = a / b
    return ans


def add(a, b):
    ans = a + b
    return ans


c = 0
d = 1

menu = {
    '1': 'add',
    '2': 'divide',
    '3': 'multiply',
    '4': 'subtract',
}

choice = ''
selection = '1'
while selection != '0':
    if selection == '1':
        for i, j in menu.items():
            print(f'{i}: {j}')
        choice = input('please choose an operation,'
                       ' press 0 to exit: ')
        if choice == '0':
            break
    if selection == '2' or choice != '':
        c = int(input('enter your first number '))
        d = int(input('enter your second number '))
        operation = {'1': add(c, d),
                     '2': divide(c, d),
                     '3': multiply(c, d),
                     '4': subtract(c, d),
                     }
        answer = operation[choice]
        print(f'ans: {answer}')
    selection = input('press 1 to switch operations,'
                      'press 2 to enter new values,'
                      'press 0 to terminate '
                      )
    