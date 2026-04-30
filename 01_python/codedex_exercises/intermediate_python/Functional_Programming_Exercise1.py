# Aufgabe
"""
Now that you can tell the difference between pure and impure functions, let’s try it out.

Create a pure function to calculate the area of a circle given its radius.

    Define a calculate_circle_area() function that takes the radius of the circle as input.
    Compute the area of the circle using the formula: area=π∗r2.
    Return the result.

"""
import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Test the function
radius = 5 
area1 = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} cm is: {area1} cm²")