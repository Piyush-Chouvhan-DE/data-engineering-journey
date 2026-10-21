import csv
from pathlib import Path

print("script started")

file_path = Path(__file__).parent/"employees.csv"
print("CSV path:",file_path)
print("File exists:", file_path.exists())

with open(file_path,"r",newline="",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

print("Script finished")

#CSV rows as dictionaries

with open(file_path,"r",newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["salary"]) > 50000: 
            print(row)
            print("Name:",row["name"])
            print("Department:", row["department"])

# Write filtered data to a new CSV file
folder = Path(__file__).parent
input_file = folder / "employees.csv"
output_file = folder / "high_salary_employees.csv"

fieldnames = ["name","department","salary"]

with open(input_file,"r",newline="",encoding="utf-8") as source:
    reader = csv.DictReader(source)

    with open(output_file,"w",newline="",encoding="utf-8") as write_file:
                writer = csv.DictWriter(write_file, fieldnames = fieldnames)
                writer.writeheader()

                # 1.write the header here 
                for row in reader:
                       print(row)
                       if int(row["salary"]) > 50000:
                            print("Matched employee:", row["name"])
                            writer.writerow(row)






        
        
        