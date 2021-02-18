import os
import shelve

hello_file = open('hello.txt')  # opens a file in read mode
content = hello_file.read()  # returns single string
print(content)
hello_file.close()  # you need to close it at the end

hello_file = open('hello.txt')
print(hello_file.readlines())  # returns list of strings
hello_file.close()

hello_file = open('hello2.txt', 'w')  # write mode (overwrites)
hello_file.write('Hello!!!')
hello_file.write('Hello!!!')
hello_file.write('Hello!!!')
hello_file.close()

bacon_file = open('bacon.txt', 'w')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

bacon_file = open('bacon.txt', 'a')  # append mode (doesnt overwrite)
bacon_file.write('\nBacon is delicious.')
bacon_file.close()

shelf_file = shelve.open('my_data')
shelf_file['cats'] = ['Panda', 'Dourado', 'Tigrado', 'Bud', 'Linda']
shelf_file.close()

shelf_file = shelve.open('my_data')
print(shelf_file['cats'])
shelf_file.close()
