#Equal or 5?

num1 = int(input('Enter the First Number : '))
num2 = int(input('Enter the Second Number : '))

dif1 = abs(num1 - num2)
dif2 = abs(num1 + num2)

if num1 == num2:
    l1 = True
    if dif1 == 5 or dif2 == 5:
        l2 = True
    else:
        l2 = False
else:
    l1 = True

if l1 == True or l2 == True:
    print('True')
else:
    print('False')


#Ravindu Rasanjana Herath
#E/23/147