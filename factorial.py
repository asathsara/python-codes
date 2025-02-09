def fact(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


user_exit = False

while not user_exit:
    number = int(input("Enter the number that you need to fin the factorial of: "))
    print(fact(number))

    print('y for yes')
    print('n for no')
    user_input = input('Do you need to exit : ')

    if user_input == 'y':
        user_exit = True
        print('Thank you for the using the FACTORIAL FINDER...')
