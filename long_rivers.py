rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
    ]
for river in rivers:
    print(river["name"])

total = 0
for river in rivers:
   total += int(river["length"])

   if river["name"][0] == "M":
       print(river["name"])
print(total)   
