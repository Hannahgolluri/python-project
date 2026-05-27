age = int(input("Enter age: "))

if age > 18:
    print("Adult")
elif age >= 13 and age <= 18:
    print("Teen")
else:
    print("Child")
