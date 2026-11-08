print("DYNAMIC MULTIPLICATION AND DIVISION TABLE")

number = float(input("Enter the number for the tables: "))
limit = int(input("Enter how far the tables should go (for example, 12): "))

print(f"\\nMULTIPLICATION TABLE FOR {number:g}")
print("-" * 35)

for i in range(1, limit + 1):
    print(f"{number:g} x {i} = {number * i:g}")

print(f"\\nDIVISION TABLE FOR {number:g}")
print("-" * 35)

for i in range(1, limit + 1):
    print(f"{number:g} / {i} = {number / i:.2f}")
