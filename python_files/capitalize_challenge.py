# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'


def capitalize (s) :
  arr = list(s)
  l = arr[0].upper()
  arr.pop(0)
  arr.insert(0, l)
  new_str = ''.join([str(e) for e in arr])
  print(new_str)



# capitalize('a short sentence')
# capitalize('a lazy fox')
capitalize('look, it is working!')