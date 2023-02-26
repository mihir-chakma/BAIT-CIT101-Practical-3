import math

# Input values
x = int(input("Enter the number of bottles filled per minute (x): "))
t = int(input("Enter the time taken to fill one bottle (t) in minutes: "))
y = int(input("Enter the total number of bottles to be filled (y): "))

# Calculate hours and minutes taken to fill y bottles
total_time = y / x * t
hours = math.floor(total_time / 60)
minutes = round(total_time % 60)

# Output the result
print(f"It takes {hours} hours and {minutes} minutes to fill {y} bottles.")

"""
we first input the values of x, t, and y using the input() function. 
Then, we calculate the total time taken to fill y bottles using 
the formula y / x * t, which gives us the time in minutes. 
We then convert this time into hours and minutes using the math.floor() and round() 
functions respectively."""

