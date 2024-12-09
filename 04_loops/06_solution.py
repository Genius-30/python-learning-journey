# Using for loop
num = int(input("Enter any number: "))
factorial = 1

for i in range(1, num+1):
  factorial *= i

print("factorial", factorial)

#---------------------------------------------------

# Using While loop
num2 = int(input("Enter any number: "))
factorial2 = 1

while num2 > 0:
  factorial2 *= num2
  num2 -= 1

print("Factorial", factorial2)