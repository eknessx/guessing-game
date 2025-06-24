fruits=["apple","banana","orange","mango"]
fruits_price=[2.50,1.80,3.00,4.50]

#fruit calculator
def get_fruit_price(fruit):
    if fruit == "apple":
        return fruits_price[0]
    elif fruit == "banana":
        return fruits_price[1]
    elif fruit == "orange":
        return fruits_price[2]
    elif fruit == "mango":
        return fruits_price[3]
    else:
        print("error choose fruit")
    

def get_quantity():
    while True:
            kg = float(input("How many kg? "))
            if kg <= 0:
                print("Please enter a positive number.")
            return kg

def calculate_total_cart():
 

    total_cart = 0
    while True:
        fruit = input("\nEnter the fruit you want to buy (or 'done' to finish): ")

        if fruit == "done":
            break

        price = get_fruit_price(fruit)

        if price is None:
            print("Invalid fruit. Please try again.")
        kg = get_quantity()
        
        # Calculate item total and add to cart
        item_total = price * kg
        total_cart += item_total
        
        # Print item details
        print(f"{fruit}: {kg} kg x ${price:.2f} = ${item_total:.2f}")
    
    # Print final cart total
    print(f"\nTotal Cart Value: ${total_cart:.2f}")
    
    euros=[50,20,10,5,1]
    for x in euros:
        euros2=0
        while total_cart >=x:
            total_cart -= x
            euros +=1
        print(f"{euros2} de {x}")



# Run the program
calculate_total_cart()