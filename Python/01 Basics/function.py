#Topic 1: Introduction to Python Functions
#Understand the syntax

def calculate_total(price, quantity):
    total = price * quantity
    return total
result = calculate_total(500,3)
print(result)

# Chellenge_1
def calculate_order_total(price, quantity):
    total = price * quantity
    return total 
result = calculate_order_total(750,4)
print(result)

#Chellenge_2

def calculate_discounted_price(price, discount_percentage):
    total = price - price * discount_percentage * .01
    return total
result = calculate_discounted_price(2000,10)
print(result)

# concept: Default parameters
def greet(name, greeting = "Hello"):
    return f"{greeting}, {name} !"
print(greet("Piyush"))
print(greet("Piyush", "Good Morning"))

#challenge_3
def calculate_final_price(price, tax_percentage = 5):
    final_price = price + price * tax_percentage * .01
    return final_price
print(calculate_final_price(1000))
print(calculate_final_price(1000,18))

#concept: Keyword arguments
print("Keyword arguments result : ",calculate_final_price(price=2000, tax_percentage=10))
print("Keyword arguments result : ",calculate_final_price(tax_percentage=10, price=2000))
print("Keyword arguments result : ",calculate_final_price(price=500))

#Mini projecet logic
def calculate_order_total(price, quantity, discount_percentage = 0):
    subtotal = (price * quantity)
    final_amount = subtotal - subtotal * discount_percentage * .01
    return final_amount
print(calculate_order_total(500, 3))
print(calculate_order_total(500, 3, 10))
print(calculate_order_total(price=1000, quantity=2, discount_percentage=15))

#concept: Local variables and scope

tax_rate = 10

def calculate_bill(price):
    discount = 100
    final_price = price - discount
    return final_price

print(calculate_bill(1000))
print(tax_rate)
#print(discount)

# challenge: Return multiple values

def calculate_bill(price, quantity):
    subtotal = price * quantity
    tax = subtotal * .05
    return subtotal, tax    

subtotal, tax = calculate_bill(1000,2)

print(subtotal)
print(tax)

# challenge 
def calculate_salary(basic_salary):
    hra = basic_salary * .2
    total_salary = basic_salary + hra 
    return total_salary, hra

total_salary, hra = calculate_salary(30000)
print(hra)
print(total_salary)
