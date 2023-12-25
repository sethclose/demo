def strings(string):
    """
    Function for Experimenting with Strings
    """
    print(f"{string}.upper() = " + string.upper())
    print(f"{string}.lower() = " + string.lower())
    print(f"{string}.split('X') = " + str(string.split('X')))
    print(f"'-'.join({string}.split('X')) = "    + '-'.join(string.split('X')))

    return

def lists(list1):
    """
    Function for Experimenting with Lists
    """
    # This is a summed comprehension
    print(f"list item length total is {sum(len(item) for item in list1)}.")
    print(f"list suffix total is {sum(int(item[-1]) for item in list1)}.")

    # Manipulating list items
    print("")
    print(f"list1[1:-1] = {list1[1:-1]}")
    print(f"list1[0:-1] = {list1[0:-1]}")
    print(f"list1[-1] = {list1[-1]}")
    print(f"list1[:] = {list1[:]}")
    print(f"list1[::2] = {list1[::2]}")
    
    print("")
    print("list1.append(list1.pop(0))")
    list1.append(list1.pop(0))
    print(f"list1 = {list1}")

    print("")
    print("list1.insert(1, list1.pop())")
    list1.insert(1, list1.pop())
    print(f"list1 = {list1}")

    print("")
    print(f"list(list1[1]) = {list(list1[1])}") 
    print(f"list(list1[1][0] = {list(list1[1][0])}") 
    print(f"list(list1[1][0][0]) = {list(list1[1][0][0])}") 

    return None

def dicts(dict1):
    """
    Function for Experimenting with Dicts
    """
    print(f"Keys: {list(dict1.keys())}")
    print(f"Values: {list(dict1.values())}")
    print(f"Items: {list(dict1.items())}")
    value1 = dict1.get("Bobo")
    print(f'value1 = dict1.get("Bobo") = {value1}')
    value1 = dict1.get("Bobo", "Missing")
    print(f'value1 = dict1.get("Bobo","Missing") = {value1}')
    return None

def build_dicts():
    """
    Function to Create and Build Dictionaries
    """
    # List to Dict to List
    user = dict([("name","Amir"), ("age",36)])
    print("user = dict([('name','Amir'), ('age',36)]) = " + str(user))
    print("list(user.items() = " + str(list(user.items())))

    # Combining Dicts
    person = {"name": "Amir"} | {"age": 36}
    print('{"name": "Amir"} | {"age": 36} = ' + str(person))

    user_data = {"name": "Betty", "mailing_list": True}
    updates = {"mailing_list": False}
    user_data = user_data | updates
    user_data["mailing_list"]
    print('{"name": "Betty", "mailing_list": True} | {"mailing_list": False} = ' + str(user_data))

    #  **, "the keyword argument unpacking syntax"
    print("** Kwarg Unpacking")
    amir_age = {"Amir": 36}
    user_ages = {**amir_age, "Betty": 41,}
    print('user_ages = {**amir_age, "Betty": 41,} = ' + str(user_ages))
    
    def build_user(name, age=None):
      return {"name": name, **({} if age is None else {"age": age}),}
    print('def build_user(name, age=None): return {"name": name, **({} if age is None else {"age": age}),}')
    print('build_user("Amir") = ' + str(build_user("Amir")))
    print('build_user("Amir", age=36) = ' + str(build_user("Amir", age=36)))

    # Other Methods
    d1 = {"a":1, "b":2, "c":3}
    print('d1 = ' + str(d1))
    d1.setdefault("b",4)
    print('d1.setdefault("b",4), d1 = ' + str(d1))
    d1.setdefault("d",4)
    print('d1.setdefault("d",4), d1 = ' + str(d1))
    d1.update({"b":4})
    print('d1.update({"b":4}), d1 = ' + str(d1))
    
    return

def dict_lists(dict_list):
    """
    Function for Experimenting with Lists of Dicts
    """
    # Numbered List of Items
    for item in enumerate(dict_list):
        #print(item)
        string = ""
        for i in item:
            if isinstance(i,int):
                string += "("+str(i)+") "
            if isinstance(i,dict):
                #string += str(i)
                string += i["name"] + " costs " + str(i["price"])
        print(string)
    # Sorted List by Price, using Lambda
    dict_list = sorted(dict_list, key=lambda item: item["price"])
    print(f"Sorted by Price: {dict_list}")
    return 
