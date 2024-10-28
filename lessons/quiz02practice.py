x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "turtle", "elephant", "fish"]
z: list[str] = ["z"]


idx: int = 0
while idx < len(z):
    print(z[idx])
    idx += 1

for i in x:
    print(i)


for i in range(0, len(x)):
    print(x[i])


my_dictionary: dict[str, float] = {}  # 10

print(my_dictionary)

msg: dict[str, int] = {"Hello": 1, "Yall": 2}  # 11

print(msg["Yall"])

msg["Yall"] += 3  # 12

ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}  # 13

ids.pop(100)

len(ids)  # 14

inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}

inventory["markers"] = 15  # 15


scores: dict[str, int] = {"alice": 85, "Bob": 90, "Charlie": 88}
