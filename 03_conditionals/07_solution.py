order_size = input("Enter coffee size (Small/Medium/Large): ").capitalize()
extra_shot = input("Enter extra short (Y/N): ").lower()

if extra_shot == "y":
  print(order_size + " coffee with an extra shot")

elif extra_shot == "n":
  print(order_size + " coffee")