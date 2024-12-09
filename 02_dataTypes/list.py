alphabets = ["a", "b", "c", "d", "e"]
print(alphabets)

print(alphabets[0])

print(alphabets[2: 4])

alphabets[2] = "C"
print(alphabets)

alphabets.append("f")
print(alphabets)

alphabets.insert(2, "C")
print(alphabets)

alphabets.remove("C")
print(alphabets)

alphabets.pop(2)
print(alphabets)

del alphabets[2]
print(alphabets)

alphabets.clear()
print(alphabets)

alphabets = ["a", "b", "c", "d", "e"]
alphabets2 = alphabets.copy()
print(alphabets2)

alphabets3 = alphabets + alphabets2
print(alphabets3)

alphabets.extend(alphabets2)
print(alphabets)

alphabets4 = alphabets * 2
print(alphabets4)

print("a" in alphabets)
print("a" not in alphabets)

for alphabet in alphabets:
    print(alphabet)

for i in range(len(alphabets)):
    print(alphabets[i])