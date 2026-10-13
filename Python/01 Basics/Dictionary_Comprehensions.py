print("  Lesson 1: Dictionary comprehensions  ")
orders = {
    "Order101": 5000,
    "Order102": 8000,
    "Order103": 3000
}


order_amount = {
    order_id : amount
    for order_id, amount in orders.items()

}
print(order_amount)

print("## practice challenge 1 ##")

orders = {
    "Order101": 2500,
    "Order102": 7500,
    "Order103": 12000,
    "Order104": 4000,
    "Order105": 9500
}

high_value_orders = {
    order_id : order_amount
    for order_id, order_amount in orders.items()
    if order_amount > 5000
}
print(high_value_orders)

print("                                           ")
print(" Challenge 2: Transform dictionary values ")

orders_usd = {
    "Order101": 100,
    "Order102": 250,
    "Order103": 150
}

orders_inr = {
    order_id : amount*85
    for order_id, amount in orders_usd.items()
    
}
print(orders_inr)

print("                                ")
print("Challenge 3: Filter and transform together")


orders = {
    "Order101": 2500,
    "Order102": 7500,
    "Order103": 12000,
    "Order104": 4000,
    "Order105": 9500
}

high_value_orders_inr = {
    order_id : round(order_amount*1.10,2)
        for order_id, order_amount in orders.items()
        if order_amount > 5000
}

print(high_value_orders_inr)

print(                         )
print("  Challenge 4: Filter and convert data types  ")

orders = {
    "Order101": 2500,
    "Order102": 0,
    "Order103": 12000,
    "Order104": 4000,
    "Order105": 9500
}

valid_orders = {
    order_id : str(order_amount)
    for order_id, order_amount in orders.items()
    if order_amount > 0 
}
print(valid_orders)

print(                            )
print("     Challenge 5: Apply a condition to transform values          ")

orders = {
    "Order101": 2500,
    "Order102": 7500,
    "Order103": 12000,
    "Order104": 4000,
    "Order105": 9500
}

order_categories = {
    order_id: "High Value" if order_amount >= 10000 else "Standard"
    for order_id, order_amount in orders.items()
}

print(order_categories)


print(                                     )
print("  Challenge 5: assigning a category ")

orders = {
    "Order101": 2500,
    "Order102": 7500,
    "Order103": 12000,
    "Order104": 4000,
    "Order105": 9500
}

order_categories_1 = {
    order_id: "High value" if order_amount >= 10000 else "Standard"
    for order_id, order_amount in orders.items()
}

print(order_categories_1)

print("                 ")
print(" Challenge 6: Create a dictionary from a list ")

order_ids = ["Order101", "Order102", "Order103", "Order104"]
order_status = {
    order_id: "Completed"
    for order_id in order_ids
}
print(order_status)

print(                        )
print(" Challenge 7: Generate values dynamically ")
numbers = [ 1,2,3,4,5]
squares = {
    number: number*number
    for number in numbers
}
print(squares)

print("                          ")
print("Challenge 8: Filter numbers and calculate their squares")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squares = {
    number: number*number
    for number in numbers
    if  number % 2 ==0
}
print(squares)



print("                              ")
print(" Challenge 9: Dictionary comprehension with strings ")

plants = ["PTC", "Paris", "Montreal", "Vacaville"]
plant_lengths = {
    plant : len(plant)
    for plant in plants 

}
print(plant_lengths)

print("                     ")
print( " Challenge 10: Filter strings by length ")

plants = ["PTC", "Paris", "Montreal", "Vacaville", "St. Mary"]

long_plant_names = {
    plant : len(plant)
    for plant in plants 
    if len(plant) > 5
}
print(long_plant_names)

print("                      ")
print(" Challenge 11: Build a dictionary from two lists ")

order_ids = ["Order101", "Order102", "Order103"]
amounts = [2500, 7500, 12000]

order_amounts = {
   order_id : amount 
   for order_id, amount in zip(order_ids, amounts)
   
}

print(order_amounts)

print(                         )

order_ids = ["Order101", "Order102", "Order103", "Order104"]
amounts_check = [2500, 7500, 12000, 4000]
high_value_orders = {
     order_id : amount_1 
    for order_id, amount_1 in zip(order_ids, amounts_check)
    if amount_1 > 5000
}
print(high_value_orders)