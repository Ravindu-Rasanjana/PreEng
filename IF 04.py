#Guess My Number Game

num = 4
print('Guess My Number Game')
gnum = int(input('Enter a number between 1 and 10 : '))

if 0 < gnum < 11:
    if gnum < num:
        print('Too Low!')
    if gnum > num:
        print('Too high')
    if gnum == num:
        print('Hooray! You Won!')
else:
    print('Invalid')

#Ravindu Rasanjana Herath
#E/23/147