# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

def chunk (arr, num):
  lists = []
  length = int(len(arr)/2)
  print(length)
  for i in range (num):
    for j in range(i):
      for k in range(i, num):
        lists.append(arr[j:num])
        lists.append(arr[k:num])
  return print(lists)

chunk([1, 2, 3, 4], 2)
# chunk([1, 2, 3, 4, 5], 2)
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3)
# chunk([1, 2, 3, 4, 5], 4)
# chunk([1, 2, 3, 4, 5], 10)