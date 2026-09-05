import math
# from math import sin, cos
name = "Jesse Rogers"
age = 48
height = 5.7555
favorite_color = "Purple"

print(name)
print(age)
print(height)
print(favorite_color)

print(name,age,height,favorite_color)

print(f"My name is {name},my favorite color is {favorite_color}, my height is {height:.2f}, my age is {age:05d}")

name1 = """Multi
line
String"""
print(name1)
print(f"""Name:{name}
age:{age}
height:{height:.2f}
fave color:{favorite_color}""")

#r = int(input("Enter a radius: "))
r = 10
circle_area = math.pi * math.pow(height, 2)
print(f"Circle area with radius {r} is {circle_area:.1f}")

print(f"the square root of my age is: {math.sqrt(age)}")


print(f"sin of height: {math.sin(height):.2f}, cos of height: {math.cos(height):.2f}")
# the sum of age and 5
print(f"Sum of age and 5: {age + 5}")

print(f" the difference of my height and 4: {height - 4}")
print(f"the product of age and height: {age * height}")
print(f"the quotient of height and 2: {height / 2}")
print(f"the remainder of age divided by age +1: {age % (age + 1)}")
age_raised_to_2 = age**2
print(f"age raised to the power of 2: {age_raised_to_2}")

temp_farenheit = float(input(f"{name} enter a temperature in Farenheit :"))
celsius = (temp_farenheit -32) * (5/9)
print(f"temp farenheit {temp_farenheit} °F in Celsius: {celsius}°C")
