from pathlib import Path

file_path = Path(__file__).parent / "skill.txt"

#1. write - replaces existing content 
with open (file_path ,"w", encoding="utf-8") as file:
    file.write("Python\nSQL\nData Engineering\n")

#2 Read - gets all lines as a list
with open(file_path, "r", encoding="utf-8") as file:
    content = file.readlines()
    print(content)

#3 Append - adds content to the end 
with open(file_path,"a",encoding="utf-8") as file:
    file.write("Git\n")
#4 Read again - verify updated content 
with open(file_path,"r",encoding="utf-8") as file:
    print(file.readlines())