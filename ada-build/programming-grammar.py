# Ada Build 
# Intro to Python 
# Lesson 02 Assignment 

# ** LEARNING GOALS **
# Understand and identify different data types (string, integer, float).
# Assign data to variables.
# Use the print function.
# Understand and use string concatenation and string interpolation.
# Identify and debug simple syntax errors.


# Variables and Assignment
# problem 1.1
x = 5
# what value does x now hold?
5 # int

# problem 1.2
z = "Hello"
# what value does z now hold?
# Hello # str 

# problem 1.3
a = 5
b = 3.2
c = a + b
# what values does c now hold?
8.2 # float

# problem 1.4
var1 = "lawl"
var2 = "brb"
# what value does var2 now hold?
# brb # str

# problem 1.5
e = 6 + 3
# what values does e now hold?
9 # int


# problem 1.6
f = 3.5
f = f + 2
# what value does f now hold?
5.5 # float


# problem 1.7
poodle = 4
pitbull = 3
boxer = poodle + pitbull
# what value does boxer now hold? 
7

# problem 1.8
h = 5
h = h + h
# what values does h now hold?
10

# problem 1.9
j = 1
k = 2
m = 3
n = j + k + m
# what value does n now hold?
6

# problem 1.10
l = "moo"
q = "quack"
l  = q
# what value does l now hold?
# quack

# problem 1.11
r = "moo"
s = "quack"
t = "woof"
r = t
# what value does r now hold?
# woof

# problem 1.12
u = 5
u = u * 2
u = u * 2
u = u * 2
# what value does u now hold?
40

# problem 1.13
v = "b"
z = "a"
# what value does v now hold?
b

# problem 1.14
aa = 3234
bb = 2398
cc = 0
dd = (aa + bb) / cc
# what value does dd now hold?
# ZeroDivisionError 

# problem 1.15
yy = 7
zz = yy % 2
# what value does zz now hold?
# Guess: 1
print(zz)

# problem 1.16
ee = 12
ff = ee % 4
# what value does ff now hold?
0

# problem 1.17
zz = 17
hh = zz % 3
# what value does hh now hold?
2


# Operators
d = 10
e = 5.0
f = 2
g = 11.0
h = 3
i = 1.5

# problem 2.1
d + e = 15.0 
# float 

# problem 2.2 
# f + h = 5 
# int

# problem 2.3
# g + h = 14.0
# float

# problem 2.4
# d - f = 8
# int

# problem 2.5
# g - e = 16.0
# float

# problem 2.6
# (h + i) - f	= 2.5
# float

# problem 2.7 
# (d - f) + e	= 13.0
# float

# problem 2.8
# d * f = 20
# int

# problem 2.9
# g * i = 16.5
# float

# problem 2.10
# f * g = 22.0 
# float

# problem 2.11
# d / f = 5.0
# float

# problem 2.12
# d / e = 2.0
# float

# problem 2.13
# e / f = 2.5
# float

# problem 2.14 
# (g * f) / f = 11.0
# float

# problem 2.15
# (d / f) * e	= 25.0
# float

# problem 2.16
# 21 / 5 = 4.2
# float

# problem 2.17
# 14 / 5 = 2.8
# float

# problem 2.18
# 10 % 3 = 1
# int

# problem 2.19
# 20 % 2 = 0
# int

# problem 2.20			
# 4 % 5 = 4
# int
		
# problem 2.21
# 8 % 1 = 0
# int



# Strings
# problem 3.1
my_string = "I love Seattle"
my_string[7] # S

# problem 3.2
my_string = "I love Seattle"
my_string[2:4] # lo

# problem 3.3
my_string = "Ada"
my_string += " Lovelace"
# I love Seattle Lovelace

# problem 3.4
my_string = "Ada"
my_string += " codes" + " it!"
# Ada codes it!

# problem 3.5
my_string = "Ada"
(my_string + " likes to code")[4:9]
# likes

# problem 3.6
my_string = "Hello world"
"Goodbye " + my_string[6:11] + "!"
# Goodbye world!

# problem 3.7
my_string = "Hello world!"
my_string[0:5] + ", goodbye!"
# Hello, goodbye!

# problem 3.8
my_string = "Hello world!"
my_string[:1] + "i" + "!"
# Hi!

# problem 3.9
my_string = "I love Python"
my_string[7:13] + my_string[2:6] + my_string[0]
# PythonloveI

# problem 3.10
my_string = "I love Python"
"P" + my_string[8:13] + " rocks!"
# Python rocks!

# problem 3.11
my_string = "I love Python"
my_string[2:6] + my_string[7:13] + my_string[2:6]
# lovePythonlove