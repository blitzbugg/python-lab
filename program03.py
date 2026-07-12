# python program to calculate library fine

days = int(input("Enter the number of days late: "))

if days <= 0:
    print("The book returned on time. no fine.")
elif days <= 5:
    fine = days * 2
    print("The fine is: Rs", fine)
elif days <= 10:
    fine = days * 5
    print("The fine is: Rs", fine)
elif days <= 30:
    fine = days * 10
    print("The fine is: Rs", fine)
else:
    print("Membership cancelled.")
