###########################################
# Set the variables to the values listed in the instructions!
my_int=7
my_float=1.23
my_bool=True

###########################################

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int =3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

print my_int


###########################################
def spam():
    eggs = 12
    return eggs
        
print spam()

###########################################
You probably saw us use the # sign a few times in earlier exercises. 
The # sign is for comments. A comment is a line of text that Python won't try to run as code.
It's just for humans to read.
###########################################

""" Write a multi-line comment in the editor. It can be any text you'd like!
"""
###########################################
# Set count_to equal to the sum of two big numbers
a=132
b=324
count_to=a+b
print count_to

###########################################
#Set eggs equal to 100 using exponentiation on line 3!

eggs =10**2

print eggs

###########################################
#Set spam equal to 1 using modulo on line 3!

spam = 8%7

print spam
###########################################
#bringing it all together 
monty=True 
python=1.234
monty_python=1.234**2


###########################################
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter ="MONTY"[4]

print fifth_letter

###########################################
parrot="Norwegian Blue"
print len(parrot)

parrot = "Norwegian Blue"
print parrot.lower()

parrot = "norwegian blue"
print parrot.upper()

###########################################
pi=3.14
print str(3.14)

ministry = "The Ministry of Silly Walks"
print len(ministry)
print ministry.upper()
###########################################
the_machine_goes="Ping!"
print the_machine_goes
###########################################
print "Spam "+"and "+"eggs"

###########################################
print "The value of pi is around " + str(3.14)
###########################################
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

###########################################
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

###########################################
# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False
###########################################
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print using_control_once()
print using_control_again()
###########################################
def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
###########################################

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

###########################################
def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2
###########################################

def cube(number):
    return number**3

def by_three(number):
    if(number%3==0):
        return cube(number)
    else:
        return False
###########################################
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

###########################################
#Let's import only the sqrt function from math this time. (You don't need the () after sqrt in the from math import sqrt bit.)

from math import sqrt
print sqrt(25)

###########################################
#Use the power of from module import * to import everything from the math module on line 3 of the editor.

from math import *
###########################################

#Universal imports may look great on the surface, but they're not a good idea for one very important reason: they fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.

If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt and there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with the exact same name.

Even if your own definitions don't directly conflict with names from imported modules, if you import * from several modules at once, you won't be able to figure out which variable or function came from where.

For these reasons, it's best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.

#The code in the editor will show you everything available in the math module.

Click Save & Submit Code to check it out (you'll see sqrt, along with some other useful things like pi, factorial, and trigonometric functions).

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

#['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
None 

###########################################
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
###########################################
"""max()
The max() function takes any number of arguments and returns the largest one. ("Largest" can have odd definitions here, so it's best to use max() on integers and floats, where the results are straightforward, and not on other objects, like strings.)

For example, max(1,2,3) will return 3 (the largest number in the set of arguments).
"""
maximum =max(3,4,5)

print maximum
###########################################
absolute = abs(-42)

print absolute
###########################################
print type(3)
print type(2.6)
print type("fdadfnsjj")

"""
<type 'int'>
<type 'float'>
<type 'str'>
"""
###########################################

def shut_down(s):
    if(s=='yes'):
        return "Shutting down"
    elif(s=='no'):
        return "Shutdown aborted"
    else:
        return "Sorry"
###########################################
from math import *
print sqrt(13689)
###########################################
def distance_from_zero(p):
    if(type(p)==int or type(p)==float):
        return abs(p)
    else:
        return "Nope"

###########################################
