a = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

print(a)
print(a["name"])
print(a.get("age"))
print(a.get("address"))
print(a.get("address", "Unknown"))
print(a.get("city", "Unknown"))

a["age"] = 40
print(a)

a["address"] = "123 Main St"
print(a)

a.update({"city": "Boston"})
print(a)

a.pop("address")
print(a)

del a["city"]
print(a)

a.clear()
print(a)

a = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }
    
b = a.copy()
print(b)

c = dict(a)
print(c)

d = dict(name="Jane", age=25, city="Chicago")
print(d)

e = dict.fromkeys(["name", "age", "city"], "Unknown")
print(e)

for key in a:
    print(key)

for key in a:
    print(a[key])

for key in a.keys():
    print(key)