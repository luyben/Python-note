# calculaor2_input

import simplegui

# intialize globals
store = 0
operand = 0

#define function
def output():
    print "store = ", store
    print "operand = ", operand
    print ""
    
def swap():
    # swap content of store and operand
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    # add operand to store
    global store
    store = store + operand
    output()
    
def sub():
    # subtract operand from store
    global store
    store = store - operand
    output()
    
def mult():
    # mutiple store by operand
    global store
    store = store * operand
    output()
    
def div():
    # subtract operand from store
    global store
    store = store /operand
    output()
    
def enter(inp):
    global operand
    operand = float(inp)
    output
 
# create frame
frame = simplegui.create_frame("caculator", 300, 300)
    
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult",mult, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter operand", enter, 100)

frame.start()

