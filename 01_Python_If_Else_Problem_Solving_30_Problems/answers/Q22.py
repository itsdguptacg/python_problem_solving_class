a_balance=int(input("Enter account Balance : "))
w_amount=int(input("Enter Withdrawal Amount : "))
if w_amount>=0 and w_amount%100==0 and w_amount<=(a_balance-500):
    print(f"Withdrawal Successful\nRemaning Balance: {a_balance-w_amount}")
else:
    print("Not Avaliable or Invalid Input") 