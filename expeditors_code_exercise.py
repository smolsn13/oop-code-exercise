class Household:
    def __init__(self, street, city, state, num_occupants):
        self.street = street
        self.city = city
        self.state = state
        self.num_occupants = num_occupants

class Person:

    def __init__(self, first_name, last_name, street, city, state, age):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.state = state
        self.age = age

people = []

with open('DIT_INPUT_Coding_Excercise.txt', 'r') as f:

    for line in f:
        people.append(line.rstrip().split(','))
    print(people)

print(people[0][0])
