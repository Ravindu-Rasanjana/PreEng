# Electricity Bill
print('================================')
print('        Electricity Bill')
print('================================')

r1 = int(input('Enter the previous reading : '))
r2 = int(input('Enter the current reading  : '))
c_type = str(input('Enter whether you are a'
                   '\n\tD: Domestic'
                   '\n\tI: Industrial'
                   '\n\tC: Charity'
                   '\n\t : '))
units = r2 - r1
if c_type == 'D':
    if 0 < units < 30 : charge = units*5
    elif 31 < units < 60 : charge = units*7
    elif 61 < units < 90: charge = units * 12
    else: charge = units * 25
elif c_type == 'I':
    if 0 < units < 30 : charge = units*20
    elif 31 < units < 60 : charge = units*50
    elif 61 < units < 90: charge = units * 75
    else: charge = units * 125
elif c_type == 'C':
    if 0 < units < 30 : charge = units*2
    elif 31 < units < 60 : charge = units*3
    elif 61 < units < 90: charge = units * 5
    else: charge = units * 10
else: print('Invalid customer type!')
print('\tAmount to be paid (in Rupees): ', charge, '/=')



