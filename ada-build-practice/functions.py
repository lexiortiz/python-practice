# Ada Build 
# Intro to Python 
# Lesson 04 Assignment 

# ** LEARNING GOALS **
# Use common built-in functions in Python.
# Understand and use functions contained in modules.
# Understand the utility of writing functions.
# Write and use custom functions.
# Understand and define the following terms: docstring, signature, arguments, parameters, return
# Understand the results of an AssertionError.

# flipside
def flipside(s):
  """
  input: string s
  output: string whose first half is s' second half and whose second half is s' first half
  """
  # find half the length of string, cut string at middle
  # len() returns number of items in string
  s_length = len(s)
  # dividing the length of the string by 2 gives us the middle
  middle = int(s_length / 2)

  # return characters from middle to end of string
  # + returns the concatenation of the strings
  return f"{s[middle:s_length]}{s[0:middle]}"


# Tests below, do not change
assert flipside(
    'carpets'
) == 'petscar', f"Reported {flipside('carpets')} for flipside('carpets') instead of petscar"
assert flipside(
    'homework'
) == 'workhome', f"Reported {flipside('homework')} for flipside('homework') instead of workhome"
assert flipside(
    'ada'
) == 'daa', f"Reported {flipside('ada')} for flipside('ada') instead of daa"

# # If the program gets here, the code works!
print("Your solution works!")

