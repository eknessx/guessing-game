#Pour la liste de bt1dev = ["Celine", "Charbel", "Elia", "Jason", "Majd"]
bt1dev = ["Celine", "Charbel", "Elia", "Jason", "Majd"]

for i in range(len(bt1dev)):
    print(i, bt1dev[i])

bt1dev[0], bt1dev[-1] = bt1dev[-1], bt1dev[0]
print(bt1dev)