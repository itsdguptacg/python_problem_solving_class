s_age = int(input("Enter the Age: "))
s_mark = int(input("Enter Marks: "))
s_att = int(input("Enter attendence percentage: "))
s_inc = int(input("Enter Family Income: "))

if 18 <= s_age <= 25 and s_mark >= 85 and s_att >= 75 and s_inc <= 300000:
    print("Scholarship Approved")
elif not (18 <= s_age <= 25):
    print("Scholarship Rejected\nReason: Age not in range of 18 to 25")
elif s_mark < 85:
    print("Scholarship Rejected\nReason: Marks below 85")
elif s_att < 75:
    print("Scholarship Rejected\nReason: Attendance below 75%")
elif s_inc > 300000:
    print("Scholarship Rejected\nReason: Family income above ₹300000")