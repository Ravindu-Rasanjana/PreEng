# Electricity Bill

print('================================')
print('       Electricity Bill')
print('================================')

units = int(input('Enter the no. of units : '))

if 0 < units < 30:
    bill = units * 5
elif 31 < units < 60:
    bill = units * 7
elif 61 < units < 90:
    bill = units * 12
else:
    bill = units * 25
print('Your bill is : Rs.', bill)

# Ravindu Rasanjana Herath
# E/23/147