# Taking user input for the area of the room
area = float(input("Enter the area of the room in square feet: "))

# Calculating the length of a side of the square room by taking square root of the area
length = round((area ** 0.5), 2)

# Displaying the result to the user
print(f"The length of each side of the square room is {length} feet.")


"""
In this code, we take user input for the area of the room using the input() function and 
convert the input to a floating-point number using the float() function. 
We then calculate the length of a side of the square room by taking the square root of the area 
using the exponent operator **. We round the length to 2 decimal places using the round() function. 
Finally, we display the result to the user using the print() function 
along with an f-string that includes the value of the length variable.
"""

