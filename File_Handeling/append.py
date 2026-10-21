from pathlib import Path

file_path = Path(__file__).parent / "output.txt"
with open(file_path, "a" , encoding="utf-8") as file:
    content = file.write("\nI am practising file handling in Python")

