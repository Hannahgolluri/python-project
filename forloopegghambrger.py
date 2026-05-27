# Eggs → add flour
eggs = [1, 2, 3]
for egg in eggs:
    print("For each egg: add 2 cups of flour")

print("-----")

# Packages → add weight
packages = [1, 2]
for package in packages:
    print("For each package: add 2 kg to truck")

print("-----")

# Burgers → reduce inventory
inventory = 10
orders = [1, 2, 3, 4]

for burger in orders:
    inventory = inventory - 1
    print("Burger sold! Inventory now:", inventory)

print("Final inventory:", inventory)
