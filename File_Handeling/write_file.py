from pathlib import Path

file_path = Path(__file__).parent/ "output.txt"

with open(file_path, "w", encoding="utf-8") as file:
    content = file.write("I am learning file handiling for Data Engineering")
    print(content)