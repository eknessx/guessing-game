def Calc_area(length,width):
    area=length*width
    return area


def Calc_perimeter(length,width):
    perimiter=2*(length+width)
    return perimiter


length=float(input("enter the width "))
width=float(input("enter the height "))



area_result=Calc_area(length,width)
area_perimi=Calc_perimeter(length,width)

print(f"the area the rectangle is:{area_result}")
print(f"the parimeter the rectangle is:{area_perimi}")