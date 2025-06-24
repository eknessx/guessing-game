import random

data={
    "customer1":{
        "cpu":"ryzen 7 5700x3d",
        "gpu":"rtx 3070",
        "ram":"crosshair vengence ddr5 16g",
        "ssd":"curcial  p560 1T ssd",
        "case":"lian lee case",
        "fans":"therminal assasin",
        "psu":"vetro 850w 600w",
        "motherboard":"asus rog b58",
    },
    "customer2":{
        "cpu":"ryzen 7 7800x3d",
        "gpu":"RX 7900 xtx",
        "ram":"crosshair vengence ddr5 32g",
        "ssd":"curcial  p560 2T ssd",
        "case":"nzxt flow h180",
        "fans":"crosshair p580",
        "psu":"vetro 850w 600w",
        "motherboard":"asus rog b580",
    },
    "customer3":{
        "cpu":"ryzen 5 7800x",
        "gpu":"rtx 5070",
        "ram":"corsshair 16g",
        "ssd":"1TB samsung",
        "case":"nzxt flow h180",
        "fans":"lain lee fans",
        "mother":"msi b580",
    },
    "prices":{
        "cpu": (180, 250),
        "gpu": (300, 1200),
        "ram": (60, 100),
        "ssd": (50, 90),
        "case": (35, 80),
        "fans": (80, 150),
        "psu": (70, 100),
        "motherboard": (200, 300),
    },
}


def calc_cost(customerkey):
    total=0
    prices=data["prices"]
    consumer=data[customerkey]

    print(f"\nEstimating prices for {customerkey}....\n")
    for part in prices:
        if part in prices:
            low,high=prices[part]
            randomprice=random.randint(low,high)
            print(f"{part.capitalize()}:{randomprice}")
            total+=randomprice
        else:
            print(f"Price not found for: {part}")
    print(f"\nEstimated Total: ${total}")
    

calc_cost("customer1")
calc_cost("customer2")
calc_cost("customer3")
