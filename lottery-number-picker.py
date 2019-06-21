import random
import time
import sys

again = True

#raw_input for python 2, input for python 3
initial = raw_input("Would you like me to pick some numbers? (Yes/No)")
while again == True:
    if initial in ("Yes", "yes"):
        print "Ok mate, winning numbers incoming..."
        #sleep comes from the time library, delays random number generation by 2 seconds cause it looks better
        time.sleep(1)
        print (random.sample(xrange(1,59), 6))
        time.sleep(0.8)
        reroll = raw_input("Would you like to me pick different numbers? (Yes/No)")
        if reroll in ("Yes","yes"):
            again == True
        else:
            print("Ok, I'll be here if ya need me :)")
            #exit the program using exit function from sys library
            sys.exit()
    elif initial in ("No", "no"):
        print ":( Maybe some other time then!"
        again = False
    else:
        initial = raw_input("Sorry, I am but a simple program and I only understand \"Yes\" or \"No\" responses :( Would you like me to pick some numbers? (Yes/No)")