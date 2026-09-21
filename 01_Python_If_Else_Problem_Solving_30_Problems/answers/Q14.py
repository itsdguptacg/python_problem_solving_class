c_price=int(input("Enter Cost Price : "))
s_price=int(input("Enter Selling Price : "))
if c_price<s_price:
    print(f"Profit = {s_price-c_price}")
elif s_price<c_price:
    print(f"Loss = {c_price-s_price}")
else:
    print("No Profit or Loss")