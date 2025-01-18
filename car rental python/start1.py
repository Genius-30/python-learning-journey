import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

print("Welcoe to the project work of: \n"
      "Aman Mondal\n")

print("Welcome to the A1 CARD Rentals")

def addUser():
  uid = input("Enter User ID: ")
  uname = input("Enter User Name: ")
  pwd = input("Enter Password: ")
  udf = pd.read_excel("Users.xlsx")
  n = udf["User ID"].count()
  udf.loc[n] = [uid, uname, pwd]
  udf.to_csv("User.xlsx", index=False)
  print("User added successfully")
  print(udf)

def deleteUser():
  uid = input("Enter a User ID: ")
  udf = pd.read_csv("Users.csv")
  udf = udf.drop(udf[udf["User ID"] == uid].index)
  udf.to_csv("Users.csv", index=False)
  print("User deleted successfully")
  print(udf)

def addNewCar():
  carno = int(input("Enter a Car Number: "))
  carname = input("Enter Name of the Car: ")
  brand = input("Enter brand of the Car: ")
  branch = input("Enter branch: ")
  fueltype = input("ENter fuel type of the car: ")
  cost = int(input("Enter cost of rent per day: "))
  category = input("Enter category of the car: ")
  cdf = pd.read_csv("Cars.csv")
  n = cdf["Car No."].count()
  cdf.loc[n] = [carno, carname, brand,branch, fueltype, cost, category]
  cdf.to_csv("Cars.csv", index=False)
  print("Card added successfully!")

def showCharts():
  print("Press 1 - Cars and their Rental Cost")
  print("Press 2 - Number of Cars booked by members")
  ch = int(input("Enter your choice: "))

  if ch == 1:
    df = pd.read_csv("Cars.csv")
    df = df[["Car Name", "Cost"]]
    df.plot("Car Name", "Cost", kind="bar")
    plt.xlabel("carname ---->")
    plt.ylabel("cost------>")
    plt.show()

  if ch == 2:
    df = pd.read_csv("Members.csv")
    df = df[["No. of cars booked", "M Name"]]
    df.plot("M Name", "No. of cars booked", kind = "bar", color="red")
    plt.show()

pressNo = int(input("Enter number: "))

if pressNo == 1:
  addUser()
elif pressNo == 2:
  deleteUser()
elif pressNo == 3:
  addNewCar()
elif pressNo == 4:
  showCharts()