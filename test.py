glbl_var = 0
# when you want to update the values of global variables,
# always first define it within function by using global command.

def function1():
    global glbl_var
    print("this is first function")
    print(glbl_var)
    glbl_var = 10
    print('foo')
    return


def function2():
    print("this is second function")
    print(glbl_var)
    return


# function1()
function2()
function1()