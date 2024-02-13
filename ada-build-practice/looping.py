# Ada Build 
# Intro to Python 
# Lesson 05 Assignment 

# ** LEARNING GOALS **
# Define the following terms: loops, iterator, iteration, iteration variable, counter-controlled, sentinel-controlled, loop table, for loop, range, while loop, blocks
# Explain the purpose for iteration in creating programs.
# Write loops in order to prevent code duplication and repetition.
# Understand how a loop will execute the statements inside and what the resulting output will be.
# Debug code with loops.

#PRACTICE PROBLEMS

#1.) Reverse a String
def reverse_string(input):
  """
  input: any word
  output: the reverse of the word
  """
  answer = ""
  # Your code goes here
  for letter in input:
    answer = f"{answer}[::-1]"


  #  End of your code
  return answer

# Tests below, do not change
assert reverse_sting("hello") == "olleh", "Cannot reverse 'hello'"
assert reverse_string("") == "", "When given an empty string it returns an empty string, but doesn't"
assert reverse_string("racecar") == "racecar", "Cannot reverse 'racecar'"
assert reverse_string("12345") == "54321", "Cannot reverse 12345"

# If the program gets here, the code works!
print("Your solution works!")


#2.) Totaling Even Numbers
def total_even_numbers(num):
  """
  input: any number
  output: sum of all even numbers from 0 to num
  """
  sum = 0
  # Your code goes here
  for i in range(num+1):
    if i % 2 == 0:
      sum += i

  # End of your code
  return sum

# Tests below, do not change
assert total_even_numbers(6) == 12, f"Reported {total_even_numbers(6)} for total_even_numbers(6) instead of 21"
assert total_even_numbers(0) == 0, f"Reported {total_even_numbers(0)} for total_even_numbers(0) instead of 0"
assert total_even_numbers(1) == 0, f"Reported {total_even_numbers(1)} for total_even_numbers(1) instead of 0"
assert total_even_numbers(15) == 56, f"Reported {total_even_numbers(15)} for total_even_numbers(15) instead of 56"

# If the program gets here, the code works!
print("Your solution works!")