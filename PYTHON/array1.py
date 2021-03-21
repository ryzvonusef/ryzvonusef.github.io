stu=["",""]
stu1=["RIZWAN","12345"]
stu[0]=input("ENTER USERNAME: ")
stu[1]=input("ENTER PASSWORD: ")

if stu[0]==stu1[0]:
    print("USERNAME IS CORRECT")
else:
    print("USERNAME IS INVALID")

if stu[1] == stu1[1]:
    print("PASSWORD IS CORRECT")
else:
    print("PASSWORD IS INVALID")
