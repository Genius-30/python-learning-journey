fruit = input("Enter fruit name: ").lower()
color = input("Enter color of fruit: ").lower()

if fruit == "banana":
  if color == "green":
    print("Unripe")
  elif color == "yellow":
    print("Ripe")
  elif color == "brown":
    print("OverRipe")