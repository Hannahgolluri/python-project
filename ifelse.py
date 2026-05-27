# Take input marks from user
marks = int(input("Enter your marks: "))

# Check conditions using if-elif-else
if marks < 35:
    print("Result: FAIL")
elif marks >= 35 and marks < 60:
    print("Result: PASS")
elif marks >= 60 and marks < 80:
    print("Result: AVERAGE")
elif marks >= 80 and marks <= 100:
    print("Result: DISTINCTION")
else:
    print("Invalid marks (should be 0 to 100)")
