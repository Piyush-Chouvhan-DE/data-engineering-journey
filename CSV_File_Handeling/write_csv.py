import csv 
from pathlib import Path

file_path = Path(__file__).parent/"new_employees.csv"

fieldnames = ["name","department","salary"]

employees = [
    {"name": "Neha", "department": "QA", "salary": 48000},
    {"name": "Karan", "department": "Data Engineering", "salary": 65000},
    {"name": "Meera", "department": "Development", "salary": 58000}
]

with open(file_path,"w",newline="",encoding="utf-8") as write_file:
                writer = csv.DictWriter(write_file, fieldnames = fieldnames)
                writer.writeheader()

                writer.writerows(employees)
