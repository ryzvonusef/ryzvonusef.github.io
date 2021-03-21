Current_Units=float(input("enter current units: "))
Previous_Units= float(input("enter previous units: "))

Units_Consumed=Current_Units-Previous_Units
print("Consumed Units: " + str(Units_Consumed))

if(Units_Consumed<=100):
    Cost=Units_Consumed*3
elif(Units_Consumed<=200):
    Cost=(100*3)+((Units_Consumed-100)*6)
else:
    Cost=(100*3)+(100*6)+((Units_Consumed-200)*12)
print("Bill is: " + str(Cost))

