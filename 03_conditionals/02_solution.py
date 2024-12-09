age = int(input("Enter your age: "))
day = input("Enter day: ")

ticketPrice = 12 if age >= 18 else 8

if(day == "wednesday"):
  ticketPrice -= 2

print("Ticket Price: ", ticketPrice)