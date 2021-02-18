import os

total_size = 0
working_directory = os.getcwd()

for file in os.listdir(working_directory):
    file_path = os.path.abspath(file)
    if not os.path.isfile(file_path):
        continue
    total_size += os.path.getsize(file_path)

print(total_size)
