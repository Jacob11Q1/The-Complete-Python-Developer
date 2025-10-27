# --------------------------------------
# Expressions vs Statements in Python
# --------------------------------------

# A statement is like a complete instruction for Python to do something.
# An expression is something that produces a value.

# Example Statement: variable assignment
iq = 100        # This is a STATEMENT (it assigns a value to a variable)

# Example Expression: something that evaluates to a value
user_age = iq / 5   # "iq / 5" is the EXPRESSION (produces 20.0)
                    # "user_age = iq / 5" is the STATEMENT (assigns the result)

print("IQ:", iq)
print("User Age:", user_age)

print()  # spacing

# --------------------------------------
# More Expression Examples
# --------------------------------------

# Expressions can be numbers, math, strings, comparisons, etc.
print("Expression examples:")
print(2 + 3)                 # math expression → 5
print("Hello " + "World")    # string expression → "Hello World"
print(iq > 50)               # boolean expression → True
print(user_age * 2)          # math with variable → 40.0

print()

# --------------------------------------
# More Statement Examples
# --------------------------------------

print("Statement examples:")

# if statement
if iq > 90:
    print("Genius detected!")    # statement with an expression inside

# for statement (loop)
for i in range(3):   # "range(3)" is an expression, but "for" is the statement
    print("Loop iteration:", i)

# function definition statement
def calculate_brainpower(iq_value):
    return iq_value * 2   # "iq_value * 2" is an expression

print("Calculated brainpower:", calculate_brainpower(iq))

print()

# --------------------------------------
# Wrapping it up
# --------------------------------------
print("Summary:")
print("- Statements DO things (assign, define, loop, condition).")
print("- Expressions PRODUCE values (2+3, iq/5, 'hello'+'world').")
