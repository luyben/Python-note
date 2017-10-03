# guess the number 

import simplegui
import random

# initailize global variable used in your code
inp = 0
n = 0

# helper function to initial game
def new_game(num_range):
    print "New game, range is form 0 to",num_range
    print "Number of guessing is 0" 
    print ""

# define event handlers for control panel
def num_guess():
    global n
    n += 1
    return n

def range100():
    # button that changes range to range(1,100) and restarts
    new_game(100)
    global inp 
    inp = random.randrange(0, 101)
    return inp

def range1000():
    # button that changes range to range(1,1000) and restarts
    new_game(1000)
    global inp 
    inp = random.randrange(0, 1001)
    return inp

def get_input(guess):
    # main game logic goes here
    global inp, n
    num_guess()
    print "Number of guessing is", n
    guess = int(guess)
    if guess > inp:
        print "Lower"
    elif guess < inp:
        print "Higher"
    else:
        print "Congratulations, you win!" 
    print ""


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100]", range100, 200)
f.add_button("Range is [0,1000]", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
f.start()
