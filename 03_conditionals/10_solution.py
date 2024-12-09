pet_type = input("Enter pet type: ").lower()
pet_age = int(input("Enter pet age: "))

if pet_type == "dog" and pet_age < 2:
    print("You need to eat Puppy Food")

elif pet_type == "cat" and pet_age > 5:
    print("You need to eat Senior Cat Food")