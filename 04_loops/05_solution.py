input_str = input("Enter string: ").lower()

for char in input_str:
  if input_str.count(char) == 1:
    print(char, "is first non repeatable character in", input_str)
    break
