# This program explores different operators.

# Declaring variables that we will manipulate

num1 = 42
num2 = 5

# Calculating and storing results using arithmetic operators
add = num1 + num2           # Sum
diff = num1 - num2          # Difference
prod = num1 * num2          # Product
div = num1 / num2           # Division
floor_div = num1 // num2    # Floor Division
mod = num1 % num2           # Modulo/Remainder
power = num1 ** 3           # Exponent

# Printing each result
print("Sum:", add)                      # Should output Sum: 47
print("Difference:", diff)              # Should output Difference: 37
print("Product:", prod)                 # Should output Product: 210
print("Division:", div)                 # Should output Division: 8.4
print("Floor Division:", floor_div)     # Should output Floor Division: 8
print("Modulo:", mod)                   # Should output Modulo: 2
print("Power:", power)                  # Should output Power: 74,088

# Using comparison and logical operators

is_greater = num1 > num2                # Comparison: returns True if num1 bigger.
is_equal = num1 == 42                   # Eqality check: returns True if matching.
logi_and = (num1 > 10) and (num2 > 5)   # Logical Operator: returns True if both conditions true.

# Prining boolean results

print("Is num1 > num2?", is_greater)    # Should output Is num1 > num2? True
print("Is num1 = to 42?", is_equal)     # Should ouput Is num1 = to 42? True
print("Logical AND:", logi_and)         # Should output Logical AND: False (42>10, but 5 is not greater than 5)
