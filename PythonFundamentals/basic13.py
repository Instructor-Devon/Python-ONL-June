
# VARIABLES
# string
name = "Devon is a guy"
print(type(True))
# int boolean/bool, float 

# array (list), object (dictionary)
names = [
    "Devon", "Jack", "Sebastian", "Justin"
]
names.append("Todd")
# print(names[4])
# print(len(name))
# print(len(names))

# LOOPS
# while
iterator = 0
while iterator < 3:
    # print(names)
    iterator += 1
# for i in range
#       1) range(when to stop)
#       2) range(start, when to stop)
#       3) range(start, when to stop, how much to increment)
for i in range(len(names)):
    print(i)
    print(names[i])

# for thing in things
for name in names:
    print(name)

def fizz_buzz():
    for i in range(1, 100):

        # If/Else
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print("HAHAHA")

    # if number%5 == 0 print "Buzz"
    # if number%3 and number%5 == 0 print "FizzBuzz"



# FUNCTIONS
def print_one_to(number):

    for i in range(1, number):
        print(i)


def get_max(numbers):
    # return the largest number
    # varaible to hold the current largest
    currMax = numbers[0]
    # loop it
    for num in numbers:
        if currMax < num:
            currMax = num
    return currMax

testList = [2,4,6,8,10]
largest = get_max(testList)
# print(largest)

testArr = [2,4,6]
# [4,6,2]
def shift_values_left(values):
    # wee need to store the first guy
    first = values[0]

    for i in range(len(values)-1):
        values[i] = values[i+1]

    # we need to but "first" at the end
    lastIdx = len(values)-1
    values[lastIdx] = first

shift_values_left(testArr)
# print(testArr)

baseball_player = {
    "first_name": "Sammy",
    "last_name": "Sosa",
    "number": 34,
    "teams": ["Cubs", "Expos"]
}

print(baseball_player["first_name"])

# iterating keys
for key_name in baseball_player:
    print(baseball_player[key_name])

for key_name, value in baseball_player.items():
    print(key_name, value)

seasons = ("Spring", "Summer", "Fall", "Winter")

for resultA, resultB in baseball_player.items():
    print(resultA, resultB)

spring, summer, fall, winter = seasons

print(spring)

# list comprehension
x = [ s * 2 for s in seasons ]
print(x)
