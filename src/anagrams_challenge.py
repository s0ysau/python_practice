# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False

def anagrams (one, two):
  special = "[@_!#$%^&*()<>?}{~:]"
  arr_one = [ele.lower() for ele in one if ele.strip() and ele.strip(special)]
  arr_two = [ele.lower() for ele in two if ele.strip() and ele.strip(special)]
  arr_one.sort()
  arr_two.sort()
  # print(arr_one, arr_two)
  if (arr_one == arr_two and len(arr_one) == len(arr_two)):
    return print ("True")
  else:
    return print ("False")





# anagrams('rail safety', 'fairy tales')
# anagrams('RAIL! SAFETY!', 'fairy tales') 
anagrams('Hi there', 'Bye there')