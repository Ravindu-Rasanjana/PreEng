# Quadratic Equation Solver

print('================================================')
print('Quadratic Equation Solver')
print('================================================')

print('Input the a, b and c in of (ax^2) + bx + c = 0')
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
dis = b**2-(4*a*c)
x1 = ((-b) + dis**(1/2))/(2*a)
x2 = ((-b) - dis**(1/2))/(2*a)

if dis < 0:
    print('No roots')
if dis > 0:
    print('There are 2 roots: ')
    print('              x1 = ', x1)
    print('              x2 = ', x2)
if dis == 0:
    print('There is one root: ', x1)

# Ravindu Rasanjana Herath
# E/23/147