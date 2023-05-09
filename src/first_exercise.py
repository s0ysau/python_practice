counter = 0 

while (counter < 10): 
  counter += 1
  if (counter % 2 == 0 and counter % 3 == 0):
      print("meow it's a 6")
  elif (counter % 2 == 0):
      print(f"{counter} is even")
  elif (counter % 3 == 0):
      print(f"meow. {counter} is divisible by 3")
  else:
      print(counter)
