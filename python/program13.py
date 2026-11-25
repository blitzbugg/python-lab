# Python program to demonstrate the concept of constructors and destructors in a class
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print("Vehicle object created.")

    def __del__(self):
        print("Vehicle object destroyed.")

# Creating an instance (object) of the Vehicle class
print("Enter the maximum speed of the vehicle (in km/h):")
max_speed = float(input())
print("Enter the mileage of the vehicle (in km/l):")
mileage = float(input())
car = Vehicle(max_speed, mileage)

# Accessing and printing the attributes
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Mileage: {car.mileage} km/l")
    
print("Deleting the vehicle object...")
del car  # Explicitly deleting the object to invoke the destructor
