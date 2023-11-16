# Month

print('================================')
print('             Month')
print('================================')

no = int(input('Enter the month : '))
mont = str('')
if no <= 12:
     print('\tValid Month')
     if no == 1: mont = str('January')
     elif no == 2: mont = str('February')
     elif no == 3: mont = str('March')
     elif no == 4: mont = str('April')
     elif no == 5: mont = str('May')
     elif no == 6: mont = str('June')
     elif no == 7: mont = str('July')
     elif no == 8: mont = str('August')
     elif no == 9: mont = str('September')
     elif no == 10: mont = str('October')
     elif no == 11: mont = str('November')
     else: mont = str('December')
     print('\tMonth : ', mont)
else: print('\tInvalid Month')

# Ravindu Rasanjana Herath
# E/23/147