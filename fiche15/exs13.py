#Write a Construct_dico function that:
#Receives the desired number of items n as input.
# At each step of the construction process: asks the user 'Enter the key: '.
#asks the user 'Enter the value: '. displays the intermediate dictionary.
#Returns the final dictionary as output.
#The entered numbers are treated as text! 
#Improve the program by ensuring that the entered numbers are treated 
#as real numbers (integers)!
# Use the .isnumeric() method for this.

#number input
n=int(input("how many times?"))#user input

#main function for the code
def Construct_dico(n):
        d={} # define the empty dictionary
        for x in range(n):
            key =input("enter the key ")
            value =input("enter the value ")
        
            if value.isnumeric():
                value =int(value) 
            
            d[key]=value
            print("Current dictionary:", d)  # show intermediate result
        return d
result=Construct_dico(n)
print(f"the final dictionary: {result}")