import simplegui
store = 0
Operand = 0
def output():
    print "Store = ", store
    print "Operand = ", Operand
def Add():
    global store, Operand
    store = store+Operand
    output()
def Subtract():
    global store, Operand
    store = store - Operand
    output()
def Swap():
    global store, Operand
    store, Operand = Operand, store
    output() 
def multiply():
    global store, Operand
    store = store * Operand
    output()
def enter(inp1):
    global Operand
    Operand = float(inp1)
    output()

frame = simplegui.create_frame("input",500,500)
frame.add_button('output', output,100)
frame.add_button('swap', Swap,100)
frame.add_button('Add',Add,100)
frame.add_button('Subtract', Subtract,100)
frame.add_button('Multiply', multiply,100)
frame.add_input("Enter Operand", enter,100)


frame.start()
