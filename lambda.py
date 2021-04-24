people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#Normal way
# def f(person):
#     return person["name"]

# people.sort(key=f)
# print(people)

#lambda
people.sort(key=lambda people: people["name"])
print(people)