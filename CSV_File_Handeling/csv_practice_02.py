import csv
from pathlib import Path

file_path = Path(__file__).parent/ "employees.csv"
output_path = Path(__file__).parent/"data_engieering_employees.csv"
rejected_path = Path(__file__).parent/"rejected_employees.csv"
filtered_path = Path(__file__).parent/"filtered_employee.csv"

# Calculate annual salary from monthly salary
# Convert monthly salary into annual salary
def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def validate_salary(salary):
    if not salary:
        return False

    try:
        monthly_salary = int(salary)
    except ValueError:
        return False

    if monthly_salary <= 0:
        return False

    return True

with open(file_path,"r", newline="",encoding="utf-8") as file,\
     open(output_path, "w", newline="",encoding="utf-8") as output_file,\
     open(rejected_path,"w",newline="", encoding="utf-8") as rejected_file,\
     open(filtered_path,"w",newline="",encoding="utf-8") as filtered_file:
      reader = csv.DictReader(file)

      writer = csv.DictWriter(
          output_file,
          fieldnames=["name", "department", "monthly_salary", "annual_salary"]
      )
      writer.writeheader()

      rejected_writer = csv.DictWriter(
          rejected_file,
          fieldnames=["name", "department", "salary","rejection_reason"]
      )
      rejected_writer.writeheader()

      filtered_writer = csv.DictWriter(
         filtered_file,
         fieldnames=["name", "department", "salary"]
     )
      filtered_writer.writeheader()

      employee_count = 0
      total_monthly_salary = 0
      total_annual_salary = 0
      skipped_count = 0
      total_records = 0 
      filtered_count = 0

      seen_names = set()

      for row in reader:
          total_records += 1 
          name = row["name"].strip().lower()

          if name in seen_names:
             print(f"skipping {row['name']}:duplicate employee name")
             skipped_count += 1
             rejected_writer.writerow({
                **row,
                "rejection_reason": "missing_salary"
                })
             continue
          seen_names.add(name)
          
          if not row["salary"]:
              print(f"Skipping {row['name']}: salary is missing")
              skipped_count += 1
              rejected_writer.writerow({
                  **row,
                  "rejection_reason":"missing_salary"
                  })
              continue
          try :
              monthly_salary = int(row["salary"])
          except ValueError:
            print(f"Skipping {row['name']}:invalid salary '{row['salary']}'")
            skipped_count += 1
            rejected_writer.writerow({
             **row,
            "rejection_reason": "invalid_salary"
                })
            continue
          if monthly_salary <= 0:
            print(f"Skipping {row['name']}: salary must be greater than zero")
            skipped_count += 1
            rejected_writer.writerow({
            **row,
            "rejection_reason": "non_positive_salary"
            })
            continue
          if row["department"] == "Data Engineering" and monthly_salary > 50000:
            employee_count+= 1 
            total_monthly_salary+= monthly_salary
            print(row["name"])

            annual_salary = calculate_annual_salary(monthly_salary) 
            total_annual_salary+= annual_salary
            writer.writerow({
                "name": row["name"],
                "department": row["department"],
                "monthly_salary": monthly_salary,
                "annual_salary": annual_salary
    })            


            print(f"Annual salary: ₹{annual_salary:,}")
            
          else:
            filtered_count += 1
            filtered_writer.writerow(row)

print("\n--- ETL Processing Summary ---")
print(f"Successfully processed: {employee_count}")
print(f"Rejected records: {skipped_count}")
print(f"Total qualifying employee:{employee_count}")
print(f"Total monthly salary : ₹{total_monthly_salary:,}")
print(f"Total annual salary :₹{total_annual_salary:,}" )
print(f"Skipped records due to bad salary: {skipped_count}")
print(f"Total input records:{total_records}")
print(f"Total filtered employee:{filtered_count}")

accounted_records = employee_count + skipped_count + filtered_count
print(f"Total accounted records:{accounted_records}")

if accounted_records == total_records:
   print("Reconciliation Successful : all records accounted for.")
else:
   print("Reconciliation warning: records count do not match.")





       

 
