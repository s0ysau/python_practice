# --- Directions
# Write a program that console logs the numbers
# from 1 to n. But for multiples of three print
# “fizz” instead of the number and for the multiples
# of five print “buzz”. For numbers which are multiples
# of both three and five print “fizzbuzz”.
# --- Example
#   fizzBuzz(5);
#   1
#   2
#   fizz
#   4
#   buzz

def fizzbuzz(num):
  if (num % 3 == 0 and num % 5 == 0):
    print("Fizzbuzz")
  elif (num % 3 == 0):
    print("Fizz")
  elif (num % 5 == 0):
    print("Buzz")
  else:
    print(f"{num}")

def array(arr): 
  for x in arr:
    fizzbuzz(x)

array([1,2,3,4,5,15])
