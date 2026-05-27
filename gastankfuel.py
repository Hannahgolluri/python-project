fuel = int(input("Enter fuel level (%): "))

if fuel < 10:
    print("LOW FUEL WARNING")
elif fuel < 50:
    print("Fuel is moderate")
else:
    print("Fuel is sufficient")
