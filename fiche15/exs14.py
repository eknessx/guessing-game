press=int(input("enter number of grades "))

def grade_calc(press):
        grades={} # define the empty dictionary
        total_grades=0
        for x in range(press):
            key =input("enter the grade ")
            value =input("enter the note ")
            if value.isnumeric():
                value = int(value)
            else:
                 print("Invalid number.skipping")
                 continue
            grades[key]=value
            total_grades+=value
            print("Current essay:", grades)
        if grades:
             average=total_grades/len(grades)
             scaled_20=(average/360)*20
             print(f"avrage {average}")
             print(f"final scaled note {scaled_20}")
        else:
             return None
        return grades
result=grade_calc(press)
print(f"the final dictionary: {result}")