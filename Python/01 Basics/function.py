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

print("                            ")
print(" Function Topic 7: Functions with lists ")
order_amounts = [1200, 4500, 800, 6200, 3000]
def calculate_total_orders (order_amount):
    total = sum(order_amount)
    return total
result = calculate_total_orders(order_amounts)
print(result)

# Cheallenge : create the function which can create a new list from exising one with values greater than 3000

def calculate_high_value_orders(order_amount_1):
    new_list = []

    for order_amount_1 in order_amounts:
        if order_amount_1 > 3000:
            new_list.append(order_amount_1)
    return new_list

order_amounts = [1200, 4500, 800, 6200, 3000, 7500]
print(calculate_high_value_orders(order_amounts))

#New Challenge : 

def analyze_orders (order_amounts):
    new_list = []

    for order_amount in order_amounts:
        if order_amount > 3000:
            new_list.append(order_amount)
       
    total = sum(new_list)
    count = len(new_list)

    return new_list, total, count 

order_amounts = [1200, 4500, 800, 6200, 3000, 7500, 2500]
hig_value_orders, total, count = analyze_orders(order_amounts)

print("High-value-orders:", hig_value_orders)
print("Total amount:", total)
print("Number of orders:", count )

print("                           ")
print(" Variable-length arguments (*args) ")

def find_maximum(*amount):
    max_amount = max(amount)
    return max_amount

print(find_maximum(10, 25, 7))
print(find_maximum(100, 45, 250, 80, 120))

# Practice: Calculate the average using *args
def calculate_average(*amounts):
    total = sum(amounts)
    count = len(amounts)
    average_amout = total/count
    return average_amout
print(calculate_average(10,20,30))
print(calculate_average(100,200,300,400))

# kwargs : **kwargs collects multiple keyword arguments into a dictionary.

def show_employee(**details):
    print(details)

show_employee(name="Piyush", age=32, department="QA Engineer")
show_employee(name="Rahul", age=30, department="IT")


# Challenge : Conbined *args and ** kwargs

def display_order(*details, **employee_values):
    return(details, employee_values)

print(display_order("Laptop", "Mouse", customer="Piyush", quantity=2))

print(display_order("Keyboard", price=1500))

# Lambda Function 
def double(number):
    return number * 2
print(double(10))
print(double(25)) 
    
calculate_square = lambda number: number * number

print(calculate_square(4))
print(calculate_square(7))

calculate_total = lambda price, Qunatity : price * Qunatity

print(calculate_total(250, 4))
print(calculate_total(150, 3))


calculate_discounted_price = lambda price, dicscount_percentage : price - price * dicscount_percentage * .01

print(calculate_discounted_price(1000, 10))
print(calculate_discounted_price(2000, 15))


check_stock = lambda quantity : "In stock" if quantity > 0 else "Out of stock"

print(check_stock(10))
print(check_stock(0))
print(check_stock(-2))


numbers = [ 2,4,6,8,10]
result = list(map(lambda number : number * 2, numbers))

print(result)

celsius_list = [0, 20, 30, 100]

Result = list(map(lambda celsius:((celsius * 9/5) +32),celsius_list))
print(Result)

#lambda with filters

numbers = [5, 12, 7, 20, 3, 18]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)


# lambda with map and filter
numbers = [2, 5, 8, 11, 14, 17]

result = list (
    map(
        lambda number : number * 2, 
        filter(lambda number :number % 2 ==0,numbers)
    )
)

print(result)


# New challenge 

numbers = [3, 6, 9, 12, 15, 18]

result = list(
    map(
        lambda number : number * 3,
        filter(lambda number : number > 10, numbers)
    )
)

print(result)

# greater than or equal to ₹200, then apply a 10% discount
prices = [100, 250, 400, 150, 600, 50]

result = list(
    map(
        lambda number : number - number * .1, 
        filter(lambda number: number >=200, prices)
    )
)

print(result)