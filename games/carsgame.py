#cars = ["Mercedes", "Ferrari", "Bugatti", "BMW", "Lamborghini", "Apolo"]
#carsBought = []
#foulous = 5000000
#carPrices = [90000, 300000, 5000000, 70000, 200000, 3000000]
#x = ""

#while x != "exit":
    #x = input("What do you want to do? (type help for options) ")
    #if x == "help":
        #print("buy car - buys a car")
        #print("show cars - lists all available cars")
    #elif x == "show cars":
        #print(f"available cars: {cars}\n")
    #elif x == "buy car":
        #y = ""
        #while True:
            #print(f"Money: {foulous}")
            #y = input("car ID : ")
            #if y == "exit":
                #break
            #y2 = int(y)
            #if foulous >= carPrices[y2]:
                #foulous -= carPrices[y2]
                #carsBought.append(cars[y2])
                #print(f"Your cars: {carsBought}")
            #else:
                #print("You are fa2ir sry")




cars ={
    "Mercedes":200000,
    "Ferrari":400000,
    "BMW":550000,
    "MClaren":700000,
    "Lamborghini":990000,
    "Bugatti":2100000,
}
carsBought = []
foulous = 5000000

while True:
    print(f"Bank: {foulous}")
    x = input("What do you want to do? (type help for options) ")
    if x == "help":
        print("buy car - buys a car")
        print("shows cars - lists all available cars")
        if x == "shows cars":
            print(f"available cars: {cars}\n")
    elif x == "buy car":
        g = input("car ID : ")
        if g == "exit":
            break
        if g in cars:
            if foulous >= cars[g]:
                foulous -= cars[g]
                carsBought.append(g)
                print(f"Your cars: {carsBought}")
            else:
                print("You are fa2ir sry")
        else:
            print("Car not found")
            