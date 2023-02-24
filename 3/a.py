# Taking user input for length, breadth and height
length = float(input("Enter the length of the cool box (in meters): "))
breadth = float(input("Enter the breadth of the cool box (in meters): "))
height = float(input("Enter the height of the cool box (in meters): "))

# Calculating the capacity of the cool box by multiplying its length, breadth and height
capacity = length * breadth * height

# Displaying the result to the user
print(f"The capacity of the cool box is {capacity} m³.")


"""
In this code, we take user input for the length, breadth and height of the cool box 
using the input() function and convert the input to floating-point numbers 
using the float() function. We then calculate the capacity of the cool box by 
multiplying its length, breadth and height. Finally, 
we display the result to the user using the print() function 
along with an f-string that includes the value of the capacity variable.
"""
