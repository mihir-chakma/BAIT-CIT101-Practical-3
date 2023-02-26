"""
To find the length of a 10 m cable in inches, 
we can use the conversion factor of 1m = 39.37 inches
"""

cable_length_m = 10
cable_length_inches = cable_length_m * 39.37

print(f"The length of the cable in inches is {cable_length_inches:.1f}")

cable_length_inches_rounded = round(cable_length_inches, 1)
print(f"The length of the cable in inches is {cable_length_inches_rounded}")
