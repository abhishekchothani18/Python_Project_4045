class Robot:
    # Class variable to keep track of total robots
    population = 0

    def __init__(self, name):
        self.name = name
        # Every time a new robot is made, increment the population
        Robot.population += 1

    # 1. Instance Method
    # Uses 'self' to access specific data (the robot's name)
    def say_hello(self):
        print(f"Bleep bloop! My name is {self.name}.")

    # 2. Class Method
    # Uses '@classmethod' and 'cls' to access class-level data
    @classmethod
    def get_population(cls):
        print(f"Current robot population: {cls.population}")

# --- Execution ---

# Creating two different instances
bot1 = Robot(name="R2-D2")
bot2 = Robot(name="C-3PO")

# Calling an instance method
# This is unique to each object
bot1.say_hello()
bot2.say_hello()

# Calling a class method
# This is shared across the entire class
Robot.get_population()