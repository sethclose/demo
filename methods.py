# Kwargs
def kwargs(name, *, age=0):
    """
    Function for Experimenting with Kwargs
    """
    print(name + " is " + str(age))
    return
print("\n\n######## kwargs(name, *, age=0):",kwargs.__doc__)
def call_kwargs():
    """
    Calls kwargs(name, *, age=0)
    """
    print("kwargs('Bobo'): ")
    kwargs('Bobo')
    print("kwargs('Bobo',age=15): ")
    kwargs('Bobo',age=15)
    try:
        print("kwargs('Bobo',15): ")
        kwargs('Bobo',15)
    except TypeError:
        print("TypeError because not age=15")
    return

# Lambdas
def lambdas(strings=None):
    """
    Function for Experimenting with Lambdas
    """
    if strings is None: strings = []
    print(f"strings = " + str(strings))
    strings.sort(key=lambda s: len(s), reverse=True)
    print(f"strings.sort(key=lambda s: len(s), reverse=True) = " + str(strings))
    print("")

    value_plus_two_lambda = lambda x: x + 2
    print("value_plus_two_lambda = lambda x: x + 2")
    print("value_plus_two_lambda(3) = " + str(value_plus_two_lambda(3)))
    def value_plus_two_regular(x): return x + 2
    print("def value_plus_two_regular(x): return x + 2")
    print("value_plus_two_regular(3) = " + str(value_plus_two_regular(3)))    

    # Call Function
    value = (lambda func, value: func(value))(lambda x: x**6, 2)
    print(f"(lambda func, value: func(value))(lambda x: x**6, 2) = {value}")
    print(f"(lambda x,y: x+y)(2,3) = {(lambda x,y: x+y)(2,3)}")
    print()
    
    # Filtered Lists
    num_list = [3,5,2,6,2,3,4]
    print(f"list of numbers: {num_list}")
    even_list = list(filter(lambda n: n % 2 == 0, num_list))
    odd_list =  list(filter(lambda n: n % 2 == 1, num_list))
    num_list.sort()
    print(f"sorted list of numbers: {num_list}")
    print(f"evens: {even_list}, odds: {odd_list}")    

            
    
    return

# InLine If Statements: Ternaries
def ternaries(nums=None):
    """
    Function for Experimenting with Ternaries
    """
    print(f"ternaries({str(nums)})")
    print("nums[index] = 10 if n > 10 else 0 if n < 0 else n")
    for index, n in enumerate(nums):
        nums[index] = 10 if n > 10 else 0 if n < 0 else n
    return

# Ranges
def ranges():
    """
    Function for Experimenting with Ranges
    """
    print(f"list(range(9)) = {list(range(9))}")
    print(f"list(range(-4,5,2)) = {list(range(-4,5,2))}")
    print(f"range(-5,5)[2:5] = {range(-5,5)[2:5]}")
    total = 0
    string = ""
    for index in range(5): 
        total += 100
        string += str(index)
    print(f"+100*5={total}")
    print(f"concat index={string}")
    return

# Slices
def slices():
    """
    Function for Experimenting with Slices
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    print("letters = " + str(letters))
    print("letters[:5] = " + str(letters[:5]))
    print("letters[-5:] = " + str(letters[-5:]))
    print("letters[1::2] = " + str(letters[1::2]))
    print("letters[::2] = " + str(letters[::2]))
    numbers = [1, 2, 3, 4]
    print("numbers = " + str(numbers))
    letters[::2] = numbers
    print("letters[::2] = numbers")
    print("   letters = " + str(letters))
    try:
        print("letters[::3] = numbers")
        letters[::3] = numbers
    except ValueError:
        print("   Value Error: Attempted to replace 2 values with 4")
    return

# Comprehensions
def comprehensions():
    """
    Function for Experimenting with Comprehensions
    """
    names = ["Amir", "Betty", "Cindy"]
    end_in_y = [name for name in names if name.endswith("y")]
    print("names = " + str(names))
    print('end_in_y = [name for name in names if name.endswith("y")]')
    print("end_in_y = " + str(end_in_y))
    print("")

    integers = [0, 1, 2]
    strings = ["a", "b", "c"]
    pairs = [(integer,string) for integer in integers for string in strings]
    print("integers = " + str(integers))
    print("strings = " + str(strings))
    print("pairs = [(integer,string) for integer in integers for string in strings]")
    print("   pairs = " + str(pairs))
    print("")
    
    items = [("a",1), ("b",2)]
    print("items = " + str(items))
    print("   {key: value for key, value in items} = " + str({key: value for key, value in items}))
    
    return

# Enumerate
def enum():
    """
    Function for Experimenting with Enumerate
    """
    print("list(enumerate('abcdefgh')) = " + str(list(enumerate('abcdefgh'))))
    print("{key: value for key, value in list(enumerate('abcdefgh'))} = " 
          + str({key: value for key, value in list(enumerate('abcdefgh'))}))
    return


# Sorting and Removing Duplicates from a List
def better_list():
    """
    Functional example of Comprehension with Enumeration and Slicing
    """
    the_list = [3, 6, 7, 3, 5, 4, 1, 7, 6, 2]
    print(f'the_list: {the_list}')
    print(r'better_list = sorted([value for index, value in enumerate(the_list)')
    print(r'                                 if value not in the_list[:index]])')
    better_list = sorted([value for index, value in enumerate(the_list) if value not in the_list[:index]])
    print(f'better_list: {better_list}')

# Built In Functions
def builtins():
    """
    Function for Experimenting with Built In Functions
    """
    nums = [2, 3, 1, 4]
    print("nums = " + str(nums))
    print("sum(nums) = " + str(sum(nums)))
    print("min(nums) = " + str(min(nums)))
    print("max(nums) = " + str(max(nums)))
    print("sorted(nums) = " + str(sorted(nums)))
    print("sorted('sorted') = " + str(sorted("sorted")))
    return

# Wrapping Functions
def wrappings():
    """
    Function for Experimenting with Wrapping Functions
    """
    def convert_arg_to_int(func):
        def wrapped(x):
            x_as_int = int(x)
            return func(x_as_int)
        return wrapped
    def add1(x): return x+1
    add1 = convert_arg_to_int(add1)
    print('add1("3") = ' + str(add1("3")))
    
    # Decorator
    @convert_arg_to_int
    def square(x): return x*x
    print(
    """@convert_arg_to_int
    def square(x): return x*x    """)
    print('square("3") = ' + str(square("3")))
    
    # Wrapper Lambda
    print('\nWrapper Lambda')
    print(r'def arg_to_string(func):  return lambda value: func(str(value))')
    def arg_to_string(func):
        return lambda value: func(str(value))
    @arg_to_string 
    def yell_number(value):
        return "!!! " + value + " !!!"
    print(f'yell_number(4):  {yell_number(4)}')

    return

# Variadic Functions and Calls
def variadics():
    """
    Function for Experimenting with Variadic Functions and Calls
    """
    # *Args
    def append_many(value, *lists):
        for l in lists: l.append(value)
    l1 = [1,2,3]
    append_many(4,l1)
    print('def append_many(value, *lists):   for l in lists: l.append(value)')
    print('   l1 = [1,2,3]  append_many(4,l1)  l1 = ' + str(l1))

    # **kwargs
    def list_lengths(**kwargs): return {key: len(values) for (key,values) in kwargs.items()}
    print('def list_lengths(**kwargs): return {key: len(values) for (key,values) in kwargs.items()}')
    print('   list_lengths(a=[1,2,3], b=[4,5]) = ' + str(list_lengths(a=[1,2,3], b=[4,5])))

    # *args and **kwargs
    def count_args(*args, **kwargs): return (len(args), len(kwargs))
    print('def count_args(*args, **kwargs): return (len(args), len(kwargs))')
    print('   count_args(1,2,3,name="Amir",age="36") = ' + str(count_args(1,2,3,name="Amir",age="36")))    
    arg_count = lambda *args, **kwargs: (len(args),len(kwargs))
    print('lambda *args,**kwargs: (len(args),len(kwargs)) = ' + str(arg_count(1,2,3,name="Amir",age="36")))

    # Function Calls 
    def product(*args):
      result = 1
      for arg in args:
        result *= arg
      return result
    print('product(1,2,3,4,5) = ' + str(product(1,2,3,4,5)))
    print('product([1,2,3,4,5]) = ' + str(product([1,2,3,4,5])))
    print('product(*[1,2,3,4,5]) = ' + str(product(*[1,2,3,4,5])))
    
    return