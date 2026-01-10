# def show_value():
#     x = 11 #local variables
#     print(x)

# show_value()

# x = 78 # global variables

# show_value()
x = 20;

def show_value():
    global x   # it can change the value of global
    # x = 12 # if the function have there own local varialble then the function can use there 
    # in the case there dont have any local variable then he can use global variable
    print(x)


show_value()