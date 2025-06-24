#some stupid code
def mygrade():
        grades={} # i made this stupid empty variable for a reason  
        total_grades=0 
        for x in range(1): # loop the whole code and yeah thats it 
            # if the user fail at entering it will handle it
            try:
                    user=input("enter the name ") # takes user name
                    value =float(input("enter the practice note "))  # takes the practice class note
                    grades[user]=value # for your info it make no sense to use it it just made the code worst
                    total_grades+=value
            except Exception as e:
                  print("a fucking error got raised",e) # it will display the error
            print("the curent student:",user,"Current essay:", grades)
        if grades:
             average=total_grades/len(grades)
             scaled_20=(average/360)*12 # it do the calculation
             print(f"average:{average}")
             print(f"final scaled note {scaled_20}")
        elif grades > scaled_20:
              average=total_grades/grades
              scaled_20=(average/360)*20<average # it should get it right its not that accuarate probably
              print(f"the highest grade person is ",user,"the highest grade",scaled_20)
        return grades
result=mygrade() # return the given arguments