print("The Invoice Program")
print()

customer = input("Enter customer type (r/w): ")
invoice = int(input("Enter invoice total: "))
print()


if customer.lower() == "r":
    if invoice < 100:
        discount = 0
    elif 100 <= invoice <= 249:
        discount = .1
    elif 250 <= invoice <= 499:
        discount = .2
    elif invoice >= 500:
        discount = .25
elif customer.lower() == "w":
    if invoice > 500:
        discount = .4
    elif invoice >= 500:
        discount = .5


discount_amount = invoice * discount
new_invoice = invoice - discount_amount

print(f"Invoice Total: {invoice}")
print(f"Discount percent: {discount}")
print(f"Discount amount: {discount_amount}")
print(f"New invoice total: {new_invoice}")

