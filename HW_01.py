john_name = 'John'
john_gender = False
john_age = 32
john_salary = 147.87
john_friends = ['James', 'Helen', 'Mike', 'Nick']

marta_name = 'Marta'
marta_gender = True
marta_age = 29
marta_salary = 138.2
marta_friends = ['Peter', 'Ann', 'Helen', 'Nick']


print(f"{john_name} salary is {john_salary} and {marta_name} salary is {marta_salary}")
print(f"{john_name} age is {john_age} and {marta_name} age is {marta_age}")


people_names = ['James', 'Helen', 'Mike', 'Nick', 'Peter', 'Ann', 'Helen', 'Nick']
unique_people_names = set(people_names)
print(unique_people_names)


current_location = (47.0025149, 28.8213795)
home_location = (46.4868207, 30.7055753)


john = {"full_name": 'John Doe',
        "age": 32,
        "salary": 147.87,
        "gender": False,
        "friends": ['James', 'Helen', 'Mike', 'Nick'],
        "coordinates": (47.0025149, 28.8213795)
        }


marta = {"full_name": 'Marta Doe',
        "age": 29,
        "salary": 138.2,
        "gender": True,
        "friends": ['Peter', 'Ann', 'Helen', 'Nick'],
        "coordinates": (46.4868207, 30.7055753)
        }


for key in john:
    print(f"{key} => {john[key]}")

for key in marta:
    print(f"{key} => {marta[key]}")
