class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if self.age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 1

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age in range(13):
            print("You are young.")
        elif self.age in range(13,18):
            print("You are a teenager")
        else:
            print("Your are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
    

# number of test cases
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")