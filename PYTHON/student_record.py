def student():
    a = input("Enter Student Name: ")
    b = input("Enter Student Course: ")
    c = input("Enter Student Phone: ")

    stu=["","",""]
    stu[0]=a
    stu[1]=b
    stu[2]=c
    for x in stu:
        print(x)

student()