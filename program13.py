# Python program to demonstrate the concept of constructors and destructors in a class
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print("Vehicle object created.")

    def __del__(self):
        print("Vehicle object destroyed.")