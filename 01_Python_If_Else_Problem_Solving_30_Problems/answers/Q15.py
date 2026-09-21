c_price=int(input("Enter Cost Price : "))
s_price=int(input("Enter Selling Price : "))
if c_price<s_price and c_price>0 and s_price>=0:
    profit=s_price-c_price
    print(f"Profit = {profit / c_price * 100} %")
elif s_price<c_price and c_price>0 and s_price>=0:
    loss=c_price-s_price
    print(f"Loss = {loss / c_price * 100} %")
else:
    print("No Profit or Loss or invalid Input")