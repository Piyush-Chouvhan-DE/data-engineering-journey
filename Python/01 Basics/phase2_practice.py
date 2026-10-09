
orders = ["Order101", "Order102","Order103","Order104"]

orders.remove("Order102")
orders.append("Order105")

print(orders)
print(len(orders))
##########################################################
print("Challenge 1 — Indexing and updating a list#########")

plants = ["Paris", "PTC", "St. Mary","Vacaville"]
print(plants[0])
print(plants[-1])
plants[1]= "Montreal"

print(plants)
###########################################################
print("Challenge 2 — append() and insert()################")

CBB_Orders = ["Order101","Order102"]
CBB_Orders.append("Order103")
CBB_Orders.insert(0,"Order100")
print(CBB_Orders)
##########################################################
print("Challenge 3 — extend()#######################")
      
orders1 = ["Order101","Order102"]
orders1.extend(["Order103","order104"])
print(orders1)
print(len(orders1))

############################################
print("##############Challenge 4 — remove() and pop()######################")

orders2 = ["Order101", "Order102", "Order103", "Order104"]
orders2.remove("Order102")
deleted_order = orders2.pop(1)
print(orders2)
print(deleted_order)

print("$$$$$$$$$$$$$$$ Challenge 5 — count() and index()################")

order_status = ["Pending","Completed","Pending","Shipped","Pending"]
print(order_status.count("Pending"))
print(order_status.index("Shipped"))

print("$$$$$$$$$$$$$$$Challenge 6 — copy() and clear()#################")
orders3 = ["Order101", "Order102", "Order103"]
backup_orders = orders3.copy()
orders3.clear()
print(backup_orders)
print(orders3)

print("@@@@@@@@Challenge 7 — sort() and reverse()###########")
quantities = [500, 120, 900, 300, 700]
quantities.sort()
print(quantities)
quantities.reverse()
print(quantities)

print("#########Challenge 8 — len(), in and not in###########")
plants = ["Paris", "PTC", "Montreal", "Vacaville"]
print(len(plants))
print("PTC" in plants)
print("St. Marry" not in  plants )

print("##############Challenge 9 — List slicing########")
orders = ["Order101", "Order102", "Order103", "Order104", "Order105", "Order106"]
print(orders[0:3])
print(orders[2:-2])
print(orders[-2:])

print("#########Challenge 10 — List iteration and filtering##########")
order_amounts = [500, 1500, 800, 2500, 1200]
count = 0

for amount in order_amounts:
    if amount >= 1000:
        print(amount)
        count+=1
print("Total Qualifying order:", count)    

print("#############Challenge 11 — Combined List Practice###########")

orders = ["Order101", "Order102", "Order103", "Order102", "Order104"]

print(orders.count("Order102"))
orders.remove("Order102")
orders.append("Order105")
orders.sort()
print(orders)
print(len(orders))

print("final challenge")

order_amounts = [1200, 500, 1800, 700, 1200, 2500, 500]

unique_amounts = []

for amount in order_amounts:
    if amount not in unique_amounts:
        unique_amounts.append(amount)

unique_amounts.sort()

print("Unique amounts:", unique_amounts)
print("Number of unique amounts:", len(unique_amounts))

