# This is a demonstration function, showing how to use various basic py functionality
print("""
######## Demo by Seth

      """)

# Strings
from variables import strings
print("\n\n######## strings(s):",strings.__doc__)
string = "aXbXcXd"
print(f"{string} is of type {type(string)}.")
strings(string)

# Lists
from variables import lists
print("\n\n######## lists(list1)",lists.__doc__)
l = ["item1", "item2", "item3", "item4", "item5", "item6"]
print(f"{l} is of type {type(l)}.")
lists(l)

# Dicts
from variables import dicts
print("\n\n######## dicts(dict1):",dicts.__doc__)
d = {
    "name": "Seth",
    "number": 1,
    }
print(f"{d} is of type {type(d)}.")
dicts(d)

# Building Dictionaries
from variables import build_dicts 
print("\n\n######## build_dicts():", build_dicts.__doc__)
build_dicts()

# Control Structures (List of Dicts)
from variables import dict_lists
dl = [  {   "name": "a",
            "price": 2},
        {   "name": "b",
            "price": 1},
        {   "name": "c",
            "price": 3},
     ]    
print("\n\n######## dict_lists(dl):",dict_lists.__doc__)
print(f"{dl} is of type {type(dl)}.")
dict_lists(dl)

# Math
print("\n\n######## Math:")
import math as m
print("m.ceil(m.pi) = " + str(m.ceil(m.pi)))

# Trying and Catching Exceptions
from errors import errors
print("\n\n######## errors():",errors.__doc__)
errors()

# Key Word Arguments: Kwargs!
from methods import call_kwargs
print("\n\n######## call_kwargs():",call_kwargs.__doc__)
call_kwargs()

# Lambda Functions
from methods import lambdas
print("\n\n######## lambdas(strings=None):",lambdas.__doc__)
l = ["apple", "banana", "cantelope"]
print(f"{l} is of type {type(l)}.")
lambdas(l)

# InLine If Statements: Ternaries
from methods import ternaries
print("\n\n######## ternaries(nums=None):",ternaries.__doc__)
numbers = [-12, 0, 2, 12]
print(f"{numbers} is of type {type(numbers)}.")
ternaries(numbers)
print(f"numbers = " + str(numbers))

# Ranges
from methods import ranges
print("\n\n######## ranges():",ranges.__doc__)
ranges()

# Slices
from methods import slices
print("\n\n######## slices():",slices.__doc__)
slices()

# Comprehensions
from methods import comprehensions
print("\n\n######## comprehensions():",comprehensions.__doc__)
comprehensions()

# Enumerate
from methods import enum
print("\n\n######## enum():",enum.__doc__)
enum()

# Better List
from methods import better_list
print("\n\n######## enum():",better_list.__doc__)
better_list()

# Built In Functions
from methods import builtins
print("\n\n######## builtins():",builtins.__doc__)
builtins()

# Wrapping Functions
from methods import wrappings
print("\n\n######## wrappings():",wrappings.__doc__)
wrappings()

# Variadic Functions and Calls
from methods import variadics
print("\n\n######## variadics():",variadics.__doc__)
variadics()

# Dates
from dates import datetimes
print("\n\n######## datetimes():",datetimes.__doc__)
datetimes()

# Files 
from files import files
print("\n\n######## files():",files.__doc__)
files()

# Modules
from modules import mods
print("\n\n######## mods():",mods.__doc__)
mods()

# JSONS
from jsons import jsons
print("\n\n######## jsons():",jsons.__doc__)
jsons()

# RegEx
from regex import regexes
print("\n\n######## regexes():",regexes.__doc__)
regexes()

# Template (Copy for new Sections)
def template():
    """
    Function to be copied for new code sections
    """
    return
print("\n\n######## template():",template.__doc__)
template()

# Sorting and Removing Duplicates from a List
## Comprehension, Enumerate, Slicing
the_list = [3, 6, 7, 3, 5, 4, 1, 7, 6, 2]
print(f'the_list: {the_list}')
better_list = sorted([value for index, value in enumerate(the_list) if value not in the_list[:index]])
print(f'better_list: {better_list}')

# Wrapper Lambda
def arg_to_string(func):
    return lambda value: func(str(value))
@arg_to_string
def yell_number(value):
    print("!!! " + value + " !!!")
yell_number(4)











