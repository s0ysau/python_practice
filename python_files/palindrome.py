#  --- Directions
#  Given a string, return true if the string is a palindrome
#  or false if it is not.  Palindromes are strings that
#  form the same word if it is reversed. *Do* include spaces
#  and punctuation in determining if the string is a palindrome.
#  --- Examples:
#    palindrome("abba") === true
#    palindrome("abcdefg") === false

#  function palindrome(str) {
#    const res = str.toLowerCase();
#    return res.split('').every((char, i) => {
#      return char === res[res.length - i - 1];
#    });
#  }
# console.log(palindrome('Racecar'))

def palindrome (str) : 
  arr = list(str.lower())
  # array[::-1] is the method to reverse an array
  reversed_arr = arr[::-1] 
  if (arr == reversed_arr):
    print ("True")
  else:
    print ("False")

palindrome('Racecar')
palindrome("abba")
palindrome("abcdefg")
palindrome("civic")
palindrome("bowling")
palindrome("kayak")