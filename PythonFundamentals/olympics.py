students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# iterate list of dictionaries
# 1) iterate the list
for student in students:
    for k, v in student.items():
        print(f"{k} - {v}")