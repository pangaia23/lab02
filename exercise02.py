from math import pi, cos, sin, pow, exp, e

#Part 1
radius = 5   # in centimeters
volume = (4/3)*pi*radius**3  #this is cubic centimeters
print(f"the volume of a sphere with radius {radius} is {volume:.3f} centimeters cubed")

#pt. 2
x = 42
pythagorean_identity = cos(x)**2 + sin(x)**2
print(f"""Is the Pythagorean Identity True for {x}?
{"Yes" if pythagorean_identity == 1 else "No"} the Pythagorean identity was {pythagorean_identity}""")

#pt. 3
euler_number_squared = e**2
print(f"Euler's Number Squared via the exponentiation operator: {euler_number_squared:>.32f}")
euler_number_squared = pow(e, 2)
print(f"Euler's Number Squared via math.pow: {euler_number_squared:>53.32f}")
euler_number_squared = exp(2)
print(f"Euler's Number Squared via math.exp: {euler_number_squared:>53.32f}")


