u_name=input("Username : admin\nPassword : python123\n---   ---   ---\nEnter Username : ")
u_pass=input("Enter Password : ")
if u_name=="admin" and u_pass=="python123":
    print("Login Successfully")
elif u_pass!="python123" and u_name=="admin":
    print("Wrong password")
else:
    print("User Not Found")