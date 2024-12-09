score = int(input("Enter you score: "))

if score > 100:
  print("Invalid Score")

else:
  if score >= 90:
    grade = "A"

  elif score >= 80:
    grade = "B"

  elif score >= 70:
    grade = "C"

  elif score >= 60:
    grade = "D"

  else:
    grade = "F"

  print("Grade:", grade)