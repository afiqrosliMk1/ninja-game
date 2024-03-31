import os

directory_path = 'C:/Users/Afiq/Desktop/delte'

directory_contents = os.listdir(directory_path)

print("Directory contents:")
for entry in directory_contents:
    print(entry)