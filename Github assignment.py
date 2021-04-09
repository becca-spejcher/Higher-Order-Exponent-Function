import random
def exponents(x,y):
    """Write a code that will return the 5th power of a list of 10 random numbers"""
    value = pow(x,y)
    return x**y

x_values = []
for i in range(10):
    x_values.append(random.randint(1,100))
y_values = [5,5,5,5,5,5,5,5,5,5]

exponent_values = list(map(exponents,x_values,y_values))
print(x_values) # Base of exponent
print(exponent_values) # Final values