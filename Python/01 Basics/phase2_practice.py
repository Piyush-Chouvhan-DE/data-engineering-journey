
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


for amount in order_amounts:
    if amount not in unique_amounts:
        unique_amounts.append(amount)

unique_amounts.sort()
print("Unique amount", unique_amounts)
print("Number of unique amount:", len(unique_amounts))

print("########################################################")
print("Tuple_Practice")
print("#########Challenge 1 — Create and access a Tuple########")

order_info = ("Order201", "PTC", 5000)
print(order_info[0])
print(order_info[-2])
print(len(order_info))

print("###########Challenge 2 — Tuple immutability############")
plants = ("Paris", "PTC", "Vacaville")
print(plants)
#plants[1] = "Montreal"
print(plants)

print("############Challenge 3 — Tuple methods#############")
order_status = ("Pending","Completed","Pending","Shipped","Pending")
print(order_status.count("Pending"))
print(order_status.index("Shipped"))


print("############### Challenge 4 — Tuple unpacking ############")

order_info = ("Order301", "Paris", 5000)

order_id, plant, quantity = order_info

print(order_info)
print(order_id)
print(plant)
print(quantity)

print("################ Challenge 5 Tuple slicing ###############")

order_ids = ("Order101", "Order102", "Order103", "Order104", "Order105")

# 1. Print the first two order IDs
# 2. Print orders from Order103 to Order105
# 3. Print the last two order IDs
# 4. Print the total number of orders

print(order_ids[0:2])
print(order_ids[2:])
print(order_ids[-2:])
print(len(order_ids))

print("######### Combine tuple operations ########")

order_statuses = ("Pending", "Completed", "Pending", "Shipped", "Pending", "Completed")

print(order_statuses.count("Pending"))
print(order_statuses.index("Shipped"))
print("cancelled" in order_statuses)
print(len(order_statuses))

print("########### Sets ##############")
order_statuses = {"Pending", "Completed", "Pending", "Shipped", "Completed"}

print(order_statuses)
print(len(order_statuses))

print("############ Add and remove values ##############")

order_statuses = {"Pending", "Completed", "Shipped"}

# 1. Add "Cancelled" to the set.
# 2. Add "Pending" again.
# 3. Remove "Shipped" from the set.
# 4. Print the final set.
# 5. Print the number of unique statuses.

order_statuses.add("Cancelled")
order_statuses.add("Pending")
order_statuses.remove("Shipped")
print(order_statuses)
print(len(order_statuses))

print("############ challenge: Membership and set operations###########")

plants = {"Paris", "PTC", "Vacaville", "St. Mary"}

# 1. Check whether "PTC" exists in the set.
# 2. Check whether "Montreal" does not exist in the set.
# 3. Add "Montreal" to the set.
# 4. Check whether "Montreal" now exists in the set.

print("PTC" in plants)
print("Montreal" not in plants)
plants.add("Montreal")
print("Montreal" in plants)
print(plants)


print("########## challenge: Compare two sets ########")

erp_plants = {"Paris", "PTC", "Vacaville", "St. Mary"}
wms_plants = {"Paris", "PTC", "Montreal", "St. Mary"}

# 1. Plants common in both sets
print(erp_plants.intersection(wms_plants))

# 2. Plants present in ERP but missing from WMS
print(erp_plants.difference(wms_plants))

# 3. Plants present in WMS but missing from ERP
print(wms_plants.difference(erp_plants))

# 4. Plants that are preent in both the sets 
print(erp_plants.union(wms_plants))

#5. symmetric_differene()
print(erp_plants.symmetric_difference(wms_plants))


# Challenge 2 : Update a set 

# 1. Add "Montreal" and "St. Mary" to the set in one statement.
# 2. Remove "PTC" using discard().
# 3. Try discarding "Berlin", which is not present.
# 4. Print the final set and its length.

plants = {"Paris", "PTC", "Vacaville"}

plants.update(["Montreal","St. Mary"])
plants.discard("PTC")
print(plants.discard("Berlin"))
print(plants)
print(len(plants))


erp_plants = {"Paris", "PTC", "Vacaville", "St. Mary", "PTC"}
wms_plants = {"Paris", "PTC", "Montreal", "St. Mary"}

# 1. Print the unique plants in ERP.
print(erp_plants.intersection(wms_plants))

# 2. Print the plants common to both systems.
print(erp_plants.symmetric_difference(wms_plants))

# 3. Print plants present in ERP but missing from WMS.
print(erp_plants.difference(wms_plants))


# 4. Print plants present in WMS but missing from ERP.
print(wms_plants.difference(erp_plants))

# 5. Print all unique plants across both systems.
print(erp_plants.union(wms_plants))

# 6. Check whether "Vacaville" exists in ERP.
print("Vacaville" in erp_plants)


print("###################################")
print("@@@@@@@@@ Dictionaries @@@@@@@@@@@@")

order = {
    "order_id": "Order101",
    "plant": "PTC",
    "amount": 5000 
    
}

print(order.items())
print(order["order_id"])
print(order["plant"])
print(order["amount"])


order = {
    "order_id": "Order101",
    "plant": "PTC",
    "amount": 5000
}

for key, values in order.items():
    print(f"{key}: {values}")
print("#####################")

orders1 = {
    "order_id": "Order101",
    "plant": "PTC",
    "amount": 5000
}

orders1["status"] = "Pending"
orders1["amount"] = 6500
orders1["customer"] = "ABC Ltd"


for key, vlaues in orders1.items():
    print(f"{key}:{values}")


order = {
    "order_id": "Order101",
    "plant": "PTC",
    "amount": 5000
}

# 1. Add a new key
order["status"] = "Pending"

# 2. Update an existing value
order["amount"] = 6500

# 3. Add another key
order["customer"] = "ABC Ltd"

# 4. Print each key and its corresponding value
for key, value in order.items():
    print(f"{key} : {value}")



print("############ Dictionary — Challenge 3: Access values safely ############")  

order = {
    "order_id" :"Order102",
    "plant" : "Paris",
    "amount" : 7500

}

print(order["order_id"])
print(order.get("status"))
print(order.get("customer", "Unknown"))
print(order.get("status","Not Available"))


print("###################################################")

order = {
    "order_id" : "Order103",
    "plant": "PTC",
    "amount": 9000,
    "status": "Pending"
}

order["status"]= "Completed"
order["customer"] = "XYZ Ltd"
removed_plant = order.pop("plant")
print("removed plant : ", removed_plant)

for key, values in order.items():
    print(f"{key} : {values}")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

order = {
    "order_id": "Order104",
    "plant": "Paris",
    "amount": 12000,
    "status": "Shipped"
}

print("############################################")

order = {
    "order_id": "Order104",
    "plant": "Paris",
    "amount": 12000,
    "status": "Shipped"
}


for keys in order.keys():
    print(order(keys))

for value in order.values():
    print(order(value))

for key, value in order.items():
    print(f"{key}, {value}")
