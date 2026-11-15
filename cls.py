class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # instance method
    def intro(self):
        print("hello, I am", self.name)

# Object Creation
apple = fruit('Apple', 'Red')
# Calling Function
apple.intro()


class fruit:

    # Constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Object Creation
apple = fruit('Apple', 'Red')
# Calling Function
print(apple.name)



class fruit:
    # class variable
    taste = 'Sweet'

    # instance variable
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Object Creation
apple = fruit('Apple','Red')
banana = fruit('Banana', 'Yellow')

print(apple.taste)
print(apple.name, apple.color)
print(banana.name, banana.color)



