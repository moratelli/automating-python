import os

path = os.path.join("folder1", "folder2", "folder3", "file.png")  # uses \ or / depending on OS
print(path)

working_dir = os.getcwd()  # gets current working directory
print(working_dir)

absolute_path = os.path.abspath('spam.png')  # gets absolute path
print(absolute_path)

converted_relative_path = os.path.abspath('../../spam.png')  # converts relative path into absolute path
print(converted_relative_path)

# converts absolute path into relative path
converted_absolute_path = os.path.relpath('/Users/pedro/Documents/dev/automating-python/spam.png')
print(converted_absolute_path)

path_exists = os.path.exists('/Users/pedro/Documents/spam-pics')  # checks if path exists
print(path_exists)
