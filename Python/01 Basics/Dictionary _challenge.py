
orders1 = {
    "order_id": "Order101",
    "plant": "PTC",
    "amount": 5000
}

orders1["status"] = "Pending"
orders1["amount"] = 6500
orders1["customer"] = "ABC Ltd"


for key, values in orders1.items():
    print(f"{key}: {values}")


