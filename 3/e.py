"""
To find the number of hours (h) it takes a machine to fill (y) 
number of bottles when it fills (x) bottles every (t) minutes, 
we can use the following expression:

h = (y / x) * (t / 60)

In this expression, we first find the number of minutes it takes to fill (y) 
bottles by dividing (y) by (x). Then, we convert this value to hours by dividing by 60.

Here's a Python code that takes user input for (x), (t) and (y), and 
calculates the number of hours and minutes it takes to fill (y) bottles:
"""

# Taking user input for x, t and y
x = int(input("Enter the number of bottles the machine fills in a minute: "))
t = int(input("Enter the time taken to fill one bottle in minutes: "))
y = int(input("Enter the number of bottles the machine needs to fill: "))

# Calculating the number of hours and minutes
fill_time_minutes = (y / x) * t
fill_time_hours = fill_time_minutes / 60
fill_time_minutes = fill_time_minutes % 60

# Displaying the result to the user
print(f"It will take {int(fill_time_hours)} hours and {int(fill_time_minutes)} minutes to fill {y} bottles.")


"""
In this code, we take user input for (x), (t) and (y) using the input() function and 
convert the input to integers using the int() function. We then calculate the number of minutes 
it takes to fill (y) bottles using the expression (y / x) * (t) and 
store the result in fill_time_minutes. We then convert this value to hours and minutes 
by dividing by 60 and using the modulo operator %. Finally, we display the result to the user 
using the print() function along with an f-string that includes the values of fill_time_hours, 
fill_time_minutes and y.
"""
