# Electricity Bill v2.0

print('================================')
print('       Electricity Bill')
print('================================')

name = str(input('Enter your name : '))
c_id = str(input('Enter your Customer ID : '))
units = int(input('Enter the no. of units : '))

if 0 < units < 30:
    bill = units * 5
elif 31 < units < 60:
    bill = units * 7
elif 61 < units < 90:
    bill = units * 12
else:
    bill = units * 25

if bill > 400: bill *= 1.15

if bill < 100: bill += 100

print('\tName         : ', name)
print('\tCustomer ID  : ', c_id)
print('\tYour bill is : Rs.', bill)

# Ravindu Rasanjana Herath
# E/23/147