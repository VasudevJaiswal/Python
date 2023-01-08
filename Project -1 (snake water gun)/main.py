# Project 1: Snake, Water, Gun Game
# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a Python program capable of playing this game with the user.

import random
def gamewin(comp,you):
    if comp == 'you':
        return None
    elif comp == 's':
        if you == 'w':
            return True
        elif you ='g':
    
        elif comp = 'w':
            if you == 'g':
                return False
    elif you = 's':
        return True
    pass


comp = input("Computer Turn: Snake(s) Water (w) or Gun (g) ? ")

randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your's  Turn: Snake(s) Water (W) or Gun (g) ? ")
gamewin(comp,you)






