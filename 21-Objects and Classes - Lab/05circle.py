class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = (Circle.__pi * 2) * (self.diameter / 2)
        return circumference

    def calculate_area(self):
        area = Circle.__pi * (self.diameter / 2) ** 2
        return area

    def calculate_area_of_sector(self, angle):
        sector = Circle.calculate_area(self) / (360 / angle)
        return sector


circle = Circle(10)
angle = 5

# Part below is test code from example

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

#################################### TASK CONDITION ############################
'''
                                    5.	Circle
Create a class Circle. In the __init__ method, the circle should only receive 
one parameter - its diameter. Create a class attribute called __pi that is 
equal to 3.14. The class should also have the following methods:
•	calculate_circumference() - returns the circumference of the circle
•	calculate_area() - returns the area of the circle
•	calculate_area_of_sector(angle) - gives the central angle in degrees, 
returns the area that fills the sector
Notes: Search the formulas on the internet. Name your methods and 
variables exactly as in the description! Submit only the class. 
Test your class before submitting it!

_______________________________________________
Example

Test Code	(no input data in this task)

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")


Output
31.40
78.50
1.09

'''
