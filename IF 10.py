# BMI

print('================================================')
print('BMI')
print('================================================')

height = float(input('Enter your height in Meters : '))
weight = float(input('Enter your weight in Kilo Grammes : '))

bmi = weight/height**2

if bmi < 18.5:
    cat = 'UnderWeight'
if 18.5 <= bmi < 24.9:
    cat = 'Healthy Weight'
if 25 <= bmi < 29.9:
    cat = 'OverWeight'
if 30 <= bmi < 34.9:
    cat = 'Obese'
if 35 <= bmi < 39.9:
    cat = 'Severely Obese'
if bmi > 40:
    cat = 'Morbidly Obese'

print('Your BMI = ', bmi)
print('You are ', cat)

# Ravindu Rasanjana Herath
# E/23/147