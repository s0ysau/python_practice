counter = 0 

# Loop 10 times starting the counter at 0
# On each loop if the counter is even print "it's even"
# If odd, print "meow" if the number is divisble by 3
# Otherwise print nothing

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
