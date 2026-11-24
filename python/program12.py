# Python program to create a vehicle class with maximum speed, mileage as instinct attribute
class Vehicle:
    def __init__(self, max_speed, mileage):
        # Initialize instance attributes
        self.max_speed = max_speed
        self.mileage = mileage

# Creating an instance (object) of the Vehicle class
print("Enter the maximum speed of the vehicle (in km/h):")
max_speed = float(input())
print("Enter the mileage of the vehicle (in km/l):")
mileage = float(input())
car = Vehicle(max_speed, mileage)

# Accessing and printing the attributes
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Mileage: {car.mileage} km/l")