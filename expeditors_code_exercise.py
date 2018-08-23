class Household:

    with open('DIT_INPUT_Coding_Excercise.txt', 'r') as f:
        for line in f:
            print(line, end = ' ')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#     def hello(self):
#         print('Hi, I am', self.first_name, self.last_name)
#
# Household('John', 'Smith').hello()
