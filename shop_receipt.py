print("WELCOME TO CATUC SHOP")

num_items = int(input("Enter the number of different items purchased: "))

items = []
subtotal = 0.0

for serial_number in range(1, num_items + 1):
    print(f"\\nITEM {serial_number}")
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity purchased: "))
    unit_price = float(input("Enter unit price (FRS): "))

    item_total = quantity * unit_price
    subtotal += item_total

    items.append({
        "serial": serial_number,
        "name": item_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": item_total
    })

# Apply the discount rules from the class program.
if subtotal > 10000:
    discount_rate = 0.30
elif num_items > 5 and subtotal > 4000:
    discount_rate = 0.15
elif subtotal > 5000:
    discount_rate = 0.01
else:
    discount_rate = 0.0

discount = subtotal * discount_rate
amount_to_pay = subtotal - discount

# Print the receipt.
print("\\n" + "=" *  seventy if False else "")
print("=" * 72)
print("CATUC SHOP")
print("SALES RECEIPT")
print("=" * 72)
print(f"{'S/N':<6}{'DESCRIPTION':<20}{'QUANTITY':>10}{'UNIT PRICE':>16}{'TOTAL':>16}")
print("-" * 72)

for item in items:
    print(
        f"{item['serial']:<6}"
        f"{item['name']:<20}"
        f"{item['quantity']:>10}"
        f"{item['unit_price']:>16.2f}"
        f"{item['total']:>16.2f}"
    )

print("-" * 72)
print(f"{'Subtotal:':>55} {subtotal:>14.2f} FRS")
print(f"{'Discount:':>55} {discount:>14.2f} FRS")
print(f"{'TOTAL TO PAY:':>55} {amount_to_pay:>14.2f} FRS")
print("=" * 72)
print("THANK YOU FOR YOUR PATRONAGE!")
print("=" * 72)
