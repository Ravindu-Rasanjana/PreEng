# Angle Calculator

print('================================')
print('        Angle Calculator')
print('================================')

angle = float(input('Enter the Angle in degrees\t: '))

if angle > 360: angle -= 360

if angle == 0: type = str('Zero Angle')
elif 1 < angle < 89: type = str('Acute angle')
elif angle == 90: type = str('Right angle')
elif 91 < angle < 179: type = str('Obtuse angle')
elif angle == 180: type = str('Straight angle')
elif 181 < angle < 359: type = str('Reflex angle')
else : type = str('Full angle')

print('\t Type of the angle : ', type)

# Ravindu Rasanjana Herath
# E/23/147