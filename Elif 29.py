# Grade and Credits

print('================================')
print('       Grade and Credits')
print('================================')

marks = int(input('Enter the your marks : '))
gdr = str('--')
crdts = str('--')

if 35 <= marks < 39:
    gdr = str('E')
    crdts = str('--')
elif 40 <= marks < 44:
    gdr = str('D+')
    crdts = str('1.3')
elif 45 <= marks < 49:
    gdr = str('C-')
    crdts = str('1.7')
elif 50 <= marks < 54:
    gdr = str('C')
    crdts = str('2.0')
elif 55 <= marks < 59:
    gdr = str('C+')
    crdts = str('2.3')
elif 60 <= marks < 64:
    gdr = str('B-')
    crdts = str('2.7')
elif 65 <= marks < 69:
    gdr = str('B')
    crdts = str('3.0')
elif 70 <= marks < 74:
    gdr = str('B+')
    crdts = str('3.3')
elif 75 <= marks < 79:
    gdr = str('A-')
    crdts = str('3.7')
elif 80 <= marks < 84:
    gdr = str('A')
    crdts = str('4.0')
elif 85 <= marks < 100:
    gdr = str('A+')
    crdts = str('4.0')

print('\tYour Grade is :    ', gdr)
print('\tYour Credits are : ', crdts)

# Ravindu Rasanjana Herath
# E/23/147