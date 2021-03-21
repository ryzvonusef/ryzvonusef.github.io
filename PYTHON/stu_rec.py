
def cont():
    c = input("Press y to continue\n")
    if c =="y":
        option()
    else:
        exit



def student_record():
    StuID = input("Enter Student ID:\n")
    StuName = input("Enter Student Name:\n")
    StuAge = input("Enter Student Age:\n")
    StuPhone = input("Enter Student Phone Number:\n")
    StuAdd = input("Enter Student Adress:\n")

    cont()



    stu = ["","","","",""]
    stu[0] = StuID
    stu[1] = StuName
    stu[2] = StuAge
    stu[3] = StuPhone
    stu[4] = StuAdd

def course_record():
    CourID = input("Enter Course ID:\n")
    CourName = input("Enter Course Name:\n")
    CourCR = input("Enter Course Credit Hours:\n")

    cont()

    cour = ["","",""]
    cour[0] = CourID
    cour[1] = CourName
    cour[2] = CourCR

def student_course():


    StuCourID = input("Enter Student ID:\n")
    
    CourStuID = input("Enter Course ID:\n")
    
    
    stucour = ["", ""]
    stucour[0] = StuCourID
    stucour[1] = CourStuID


    cont()


def option():
    x = int(input("Which Record do you wish to enter\n1:Student Records\n2:Course Records\n3:Student Course Enrollment\n"))
    if x == 1:
        student_record()
    elif x == 2:
        course_record()
    elif x == 3:
        student_course()
    else:
        print("Please enter either 1, 2 or 3")

option()

