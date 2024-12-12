file = open('../genius.txt', 'w')

try:
    file.write('Hello world')
finally:
    file.close()

with open('../hello.txt', 'w') as file:
    file.write('Hello World')