import csv
from pathlib import Path

file_path = Path(__file__).parent/ "employees.csv"

with open(file_path,"r", newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    
    for row in reader:

        if row["department"] == "Data Engineering":
            print(row["name"])

            monthly_salary = int(row["salary"])
            annual_salary = monthly_salary * 12 

            print(f"Annual salary: ₹{annual_salary:,}")
       

 
