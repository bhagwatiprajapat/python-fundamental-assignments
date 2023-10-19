#Function with no argumant & no return value.

def printline():
    print("*"*50)

printline()
print("Welcome to user defined function in python.")
printline()

#Function with argument but no return value.

def add(a,b):
    print("addition : ",a+b)

printline()
add(23,23)
printline()

#function with argument & with return value.

def sub(a,b):
    return a-b

printline()
ans=sub(34,345)
