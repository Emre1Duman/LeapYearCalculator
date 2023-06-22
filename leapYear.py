
# if a year is evenly divisbible by 4 and not 100 then it is a leap year
# if a year is evenly divisbible by 4 and 100 then it is not a leap year, unless the year is also evenly divisble by 400 then it is


year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")


# Different method:
# if year % 4 > 0:
#     print("Not leap year.")
# elif year % 4 == 0 and year % 100 > 0:
#     print("leap year.")
# elif year % 100 == 0 and year % 400 == 0:
#     print("leap year.")
# else:
#     print("Not leap year.")











