# Taking user input for the number of boys and girls
num_boys = int(input("Enter the number of boys in the class: "))
num_girls = int(input("Enter the number of girls in the class: "))

# Calculating the total number of students
total_students = num_boys + num_girls

# Calculating the ratio of girls and boys as a percentage of the total number of students
girls_ratio = (num_girls / total_students) * 100
boys_ratio = (num_boys / total_students) * 100

# Displaying the result to the user
print(f"The ratio of girls to boys in the class is {girls_ratio:.2f}% to {boys_ratio:.2f}%.")


"""
In this code, we take user input for the number of boys and girls in the class using 
the input() function and convert the input to integers using the int() function. 
We then calculate the total number of students by adding the number of boys and girls. 
We then calculate the ratio of girls and boys as a percentage of the total 
number of students by dividing the number of girls or boys by the total 
number of students and multiplying the result by 100. We format the output to 
display the percentage with 2 decimal places using the :.2f notation within 
the f-string that includes the values of girls_ratio and boys_ratio. 
Finally, we display the result to the user using the print() function.
"""

