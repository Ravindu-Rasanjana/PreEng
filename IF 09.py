# Equal or 5?

print('================================================')
print('Equal or 5?')
print('================================================')

num1 = int(input('Enter the First Number : '))
num2 = int(input('Enter the Second Number : '))

dif1 = abs(num1 - num2)
dif2 = abs(num1 + num2)

if num1==num2 or dif1 == 5 or dif2 == 5:
    print('True')
else:
    print('False')

# Ravindu Rasanjana Herath
# E/23/147