class Greeter:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """Method 1: A friendly greeting"""
        print(f"Hello, {self.name}! Welcome to Python programming.")

    def say_goodbye(self):
        """Method 2: A simple farewell"""
        print(f"Goodbye, {self.name}! Have a great day.")

# --- Execution ---

# 1. Create an instance (object) of the class
my_greeter = Greeter("Alex")

# 2. Execute the first method
my_greeter.say_hello()

# 3. Execute the second method
my_greeter.say_goodbye()