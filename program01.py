# Check whether a given number is between a range of numbers

num = float(input("Enter a number: "))
start = float(input("Enter the starting range: "))
end = float(input("Enter the ending range: "))

if start <= num <= end:
    print("The number is within the range.")
else:
    print("The number is not within the range.")