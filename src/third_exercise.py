# sub_nums that takes two arguments and returns their difference
def add_num (num1, num2):
  return num1 + num2

print (add_num(1,2))

# say_hello that takes a name as an arguments and says hello to that name
def say_hello(name):
  return f"Hello {name}"

print (say_hello('Jerrick'))

# sayhelloadv that takes a dictionary with a name and age property and prints "hello {name}, how does it feel to be {age} years old"

input_name = input("What is your name?")
input_age = input("What is your age?")

def name_age(name, age):
  return f"Hello {name}, how does it feel to be {age} years old"

print(name_age(input_name, input_age))  

# looper takes one array as an argument, it loops over the array and prints each item individually

this_array = [1,2,3,4,5,6]

def looping(array):
  for x in array:
    print (x)

looping(this_array)

