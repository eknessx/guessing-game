def binary():
    try:
        enterx=int(input("enter a number "))
        enterz=int(input("enter a number "))
        e=enterx*enterz+1

        print(bin(e*10^0))
    except Exception as e:
        print("instance error occured",e)
binary()