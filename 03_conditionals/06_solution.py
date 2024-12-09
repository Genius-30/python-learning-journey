distance = int(input("Enter distance in KM: "))

if distance < 3:
  print("Walk")

elif distance < 15:
  print("Bike")

else:
  print("Car")