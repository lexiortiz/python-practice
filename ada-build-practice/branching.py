# Ada Build 
# Intro to Python 
# Lesson 03 Assignment 

# ** LEARNING GOALS **
# Understand and use relational operators.
# Understand and be able to use conditional statements.
# Understand the control flow of a program.
# Identify and debug simple logic errors.


# Conditionals Syntax
# Practice 1
temp = 40

if temp < 50:
    print("It's a bit chilly outside")
# It's a bit chilly outside

# Practice #2
temp = 100

if temp < 50:
    print("It's a bit chilly outside")
else:
    print("It's pleasant outside")
    # It's pleasant outside

# Practice #3
temp = 0

if temp == 100:
    print("It's ONE HUNDRED DEGREES outside!")
elif temp < 100:
    print("It's warm outside")
elif temp < 50:
    print("It's a bit chilly outside")  
elif temp == 0:
    print("It's ZERO DEGREES outside!") 
# It's warm outside
# this is a logic error

if temp == 0:
    print("It's ZERO DEGREES outside!") 
elif temp == 100:
    print("It's ONE HUNDRED DEGREES outside!")
elif temp < 50:
    print("It's a bit chilly outside") 
elif temp < 100:
    print("It's warm outside")
# It's ZERO DEGREES outside!

# Black Jack Debugging Exercise
# Fix the logic error:
score = 21

if score < 17:
    print("Hit Me!")
elif score < 21:
    print("Great Hand")
elif score >= 21:
    print("Bust!")
else:
    print("Black Jack!")

# Change to: 
if score == 21:
    print("Black Jack!")
elif score < 17:
    print("Hit Me!")
elif score < 21:
    print("Great Hand!")
else:
    print("Bust!")
#  This solution is arranged to benefit the understanding of subsequent readers.

# Divisible by 5
x = 2023

if x % 5 == 0:
    print(f"{x} is divisible by 5")
else:
    print(f"{x} is not divisible by 5")
# 2023 is not divisible by 5


# Conditionals Syntax
# Practice 1
x = 20 / 5
y = 6 * 2

if x == y:
  print('equal')
elif x < y:
  print('loss')
else:
  print('greater')

# Practice 2
if number_of_sides == 1:
    print("You've got a line")
elif number_of_sides == 2:
    print("I'm not really sure what you have")
elif number_of_sides == 3:
    print "You've got a triangle"
elif number_of_sides == 4:
    print("You've got some sort of quadrilateral")

# Is there more than one line?
# No -- you have a line.
# Yes -- Continue.
# Is there more than 2 lines?
# No -- I'm not sure what you have.
# Yes -- Continue.
# Is there more than 3 lines?
# No -- you have a triangle.
# Yes -- Continue.
# Is there more than 4 lines?
# No -- you've got some sort of quadrilateral.

# Practice 3
# problem 1
cookies = True
cake = False

if cookies:
    print("OMG COOKIEZ")

    if 

if cake:
    print("OMG CAKE!")
else:
    print("WHATEVZ DESSERTZ.")

# change to:

if cookies:
    print("OMG COOKIEZ")
elif cake:
    print("OMG CAKE!")
else:
    print("WHATEVZ DESSERTZ.")
# OMG COOKIEZ

# Is cookies true?
# Yes -- omg cookiez!
# No -- Continue.
# Is cake true?
# Yes -- omg cake!
# No -- whatevz dessert.

# problem 2
person_age = 55
ada_age = 6

if person_age < ada_age:
    print("This person is younger")
elif ada_age < person_age:
    print("Ada is younger")
else:
    print("They’re the same!")
# Ada is younger

# Is person the same age as ada?
# Yes -- they're the same!
# No -- Continue.
# Is person younger than ada?
# Yes -- person is younger.
# No -- Continue.
# Is ada younger than person?
# Yes -- ada is younger.
# No -- Continue.

# problem 3
pet = "cat"
food = "ice cream"

if pet == "cat":
    print("here kitty")
elif pet == "dog":
    print("woof")
else:
    print("some other sound")

if food == "broccoli":
    print("eh.")
elif food == "ice cream":
    print("yum")
# here kitty
# yum

# Is pet a cat?
# Yes -- here kitty
# No -- Continue.
# Is pet a dog?
# Yes -- woof
# No -- some other sound

# Is food broccoli
# Yes -- eh.
# No -- Continue.
# Is food ice cream?
# Yes -- yum.

# problem 4
x = 7
y = 7

if x >= y:
    if x > y:
        print("x is bigger")
    else:
        print("x = y")
else:
    print("y is bigger")
# x = y

# Is x greater than or = y?
# No -> y is bigger than x.
# Yes -> Is x greater than y?
    # Yes -> x is bigger 
    # No -> x = y

# problem 5
x = 7
y = 7

if x > y or x == y:
    if x > y:
        print("x is bigger")
    else:
        print("x = y")
else:
    print("y is bigger")
# x = y

# Is x greater than or = y?
# No -> y is bigger than x.
# Yes -> Is x greater than y?
    # Yes -> x is bigger 
    # No -> x = y

# problem 6
x = 7
y = 7

if x >= y:
    print("x is bigger")
else:
    print("y is bigger")

if x == y:
    print("x = y")
# x is bigger
# x = y

# Is x greater than or = y?
# No -> y is bigger than x.
# Yes -> x is bigger.

# Is x = y?
# Yes -> x = y.
# No -> do nothing. 
