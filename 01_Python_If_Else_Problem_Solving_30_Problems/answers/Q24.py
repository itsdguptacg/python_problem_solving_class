amt = float(input("Enter the Amount : "))
if amt > 0:
    if 500>=amt>=0:
        print(f"\n--- --- --- ---\nPurchased : ₹{amt:.2f}\n--- --- --- ---\nDiscount 0%\nDiscount Amount : ₹{(amt*0.00):.2f}\nFinal amount : ₹{(amt-(amt*0.00)):.2f}\n")
    elif 999>=amt>=500:
        print(f"\n--- --- --- ---\nPurchased : ₹{amt:.2f}\n--- --- --- ---\nDiscount 5%\nDiscount Amount : ₹{(amt*0.05):.3f}\nFinal amount : ₹{(amt-(amt*0.05)):.2f}\n")
    elif 1999>=amt>=1000:
        print(f"\n--- --- --- ---\nPurchased : ₹{amt:.2f}\n--- --- --- ---\nDiscount 10%\nDiscount Amount : ₹{(amt*0.10):.2f}\nFinal amount : ₹{(amt-(amt*0.10)):.2f}\n")
    elif 4999>=amt>=2000:
        print(f"\n--- --- --- ---\nPurchased : ₹{amt:.2f}\n--- --- --- ---\nDiscount 15%\nDiscount Amount : ₹{(amt*0.15):.2f}\nFinal amount : ₹{(amt-(amt*0.15)):.2f}\n")
    elif amt>=5000:
        print(f"\n--- --- --- ---\nPurchased : ₹{amt:.2f}\n--- --- --- ---\nDiscount 20%\nDiscount Amount : ₹{(amt*0.20):.2f}\nFinal amount : ₹{(amt-(amt*0.20)):.2f}\n")
else:
    print("Invalid Input")