# calculaor layout

import simplegui

# intialize globals
store = 12
operand = 3

#define function
def output():
    print "store = ", store
    print "operand = ", operand
    print ""
    
def swap():
    global store, operand
    store, operand = operand, store
    output()
def add():
    global store, operand
    store += operand
    output()
    
def sub():
    global store, operand
    store = store - operand
    output()
    
frame = simplegui.create_frame("caculator", 200, 200)
    
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)

frame.start()
