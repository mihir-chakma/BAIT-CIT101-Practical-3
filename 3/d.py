# Taking user input for principal, rate and period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): ")) / 100
period = float(input("Enter the period (in years): "))

# Calculating the simple interest
interest = principal * rate * period

# Displaying the result to the user
print(f"The simple interest is {interest:.2f} dollars.")


"""
In this code, we take user input for the principal amount, annual interest rate and 
period using the input() function and convert the input to floating-point numbers using 
the float() function. We divide the annual interest rate by 100 to convert it 
from a percentage to a decimal value. We then calculate the simple interest by multiplying 
the principal, rate and period. Finally, we display the result to the user using 
the print() function along with an f-string that includes the value of the interest 
variable formatted to 2 decimal places using the :.2f notation.
"""
