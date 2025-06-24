#creer 2 dictionares l'un contenant les noms de 3 eleves l'autres contenant les 3 notes de chacun
def grade_calc():
        grades={} # define the empty dictionary
        total_grades=0
        for x in range(3):
            key =float(input("enter the ctrl note "))
            value =float(input("enter the practice note "))
            grades=value
            total_grades+=value
            print("Current essay:", grades)
        if grades:
             average=total_grades/grades
             scaled_20=(average/360)*20
             print(f"avrage {average}")
             print(f"final scaled note {scaled_20}")
        else:
             return None
        return grades
result=grade_calc()
