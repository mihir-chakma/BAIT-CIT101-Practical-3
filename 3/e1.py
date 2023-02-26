"""
we take input values of x, t and y from the user using the input() function. 
Then, we calculate the total time in minutes it will take to fill y bottles 
using the formula (y * t) / x. Finally, we convert this time into 
hours and minutes and print the result using the print() function.
"""

x = int(input("Enter the number of bottles filled per minute (x): "))
t = int(input("Enter the time taken to fill one bottle in minutes (t): "))
y = int(input("Enter the number of bottles to be filled (y): "))

# Calculating the number of hours to fill 'y' bottles
total_time_in_minutes = y * t / x
hours = int(total_time_in_minutes / 60)
minutes = int(total_time_in_minutes % 60)

print(f"The machine takes {hours} hours and {minutes} minutes to fill {y} bottles.")

