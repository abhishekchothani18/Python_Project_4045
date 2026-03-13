# Global variable
x = 10

def outer():
    y = 20   # nonlocal variable for inner function

    def inner():
        nonlocal y
        global x

        x = x + 5        # modify global variable
        y = y + 5        # modify nonlocal variable
        z = 30           # local variable

        print("Inside inner()")
        print("Local variable z =", z)
        print("Nonlocal variable y =", y)
        print("Global variable x =", x)

    inner()
    print("\nInside outer()")
    print("Nonlocal variable y =", y)

# Function call
outer()

print("\nIn main program")
print("Global variable x =", x)
