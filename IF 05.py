#Finding the larger number

num1 = int(input('Enter the First Number : '))
num2 = int(input('Enter the Second Number : '))

if num1 != num2:
    if num1 * num2 > 0:
        if num1 > num2:
            print('Largest Number = ', num1)
        else:
            print('Largest Number = ', num2)
    if num1 * num2 < 0:
        if num1 > 0:
            print('Largest Number = ', num1)
        else:
            print('Largest Number = ', num2)
    if num1 * num2 == 0:
        print("'O' Can't be used as an input")
else:
    print('Both values are the same!')

#This program doesn't approve "0" as an input

#Ravindu Rasanjana Herath
#E/23/147