# Define a class named 'rectangle'
class rectangle():

    # Constructor (__init__) method to initialize the object with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate and return the perimeter of the rectangle
    def perimetre(self):
        return (self.length + self.width) * 2
    
    # Method to calculate and return the area of the rectangle
    def Aire(self):
        return self.length * self.width
    
    # Method to check if the rectangle is a square
    def isCarre(self):
        if self.length == self.width:
            return True
        else:
            return False
        
    # Method to display information about the rectangle
    def afficher_rectangle(self):
        print("length ", self.length)
        print("width ", self.width)
        print("perimeter ", self.perimetre())
        print("area ", self.Aire())
        if self.isCarre() == True:
            print("it's a square")
        else:
            print("it's not a square")

# Get user input for the length and width of the rectangle
length = float(input("enter the length: "))
width = float(input("enter the width: "))

# Create a rectangle object with the provided length and width
r = rectangle(length, width)

# Call the method to display information about the rectangle
r.afficher_rectangle()


