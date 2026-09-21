date=int(input("enter The date : "))
month=int(input("enter The month : "))
year=int(input("enter The year : "))
if (year%400 == 0 and year>=0) or ((year%4==0 and year%100!=0) and year>=0):
    if 1<=month<=12:
        if (month==1 and 1<=date<=31) or (month==2 and 1<=date<=29) or (month==3 and 1<=date<=31) or (month==4 and 1<=date<=30) or (month==5 and 1<=date<=31) or (month==6 and 1<=date<=30) or (month==7 and 1<=date<=31) or (month==8 and 1<=date<=31) or (month==9 and 1<=date<=30) or (month==10 and 1<=date<=31) or (month==11 and 1<=date<=30) or (month==12 and 1<=date<=31):
            print("Date is Valid")
        else:
            print("Enter Valid Date")
    else:
        print("Enter A valid Month")
elif year>=0:
    if 1<=month<=12:
        if (month==1 and 1<=date<=31) or (month==2 and 1<=date<=28) or (month==3 and 1<=date<=31) or (month==4 and 1<=date<=30) or (month==5 and 1<=date<=31) or (month==6 and 1<=date<=30) or (month==7 and 1<=date<=31) or (month==8 and 1<=date<=31) or (month==9 and 1<=date<=30) or (month==10 and 1<=date<=31) or (month==11 and 1<=date<=30) or (month==12 and 1<=date<=31):
            print("Date is Valid")
        else:
            print("Enter Valid Date")
    else:
        print("Enter A valid Month")
elif year<0:
    print("Enter a valid Year")