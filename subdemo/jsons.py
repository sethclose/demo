# JSONS
import json
def jsons():
    """
    Function for experimenting with JSONS
    """
    # Define a Dictionary
    dict_1 = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }
    print(f"dict_1: {dict_1}")

    # Convert into JSON:
    json_1 = json.dumps(dict_1)
    print(f"json_1: {json_1}")
    try:
        print(f"  json_1['age'] = {json_1['age']}")
    except TypeError:
        print(f"  json_1['age'] = TypeError")

    # Convert back to dict
    dict_2 = json.loads(json_1)
    print(f"dict_2: {dict_2}")
    print(f"  dict_2['age'] = {dict_2['age']}")

    # Other variable types
    print('json.dumps({"name": "John", "age": 30}):  ' + json.dumps({"name": "John", "age": 30}))
    print('json.dumps(["apple", "bananas"]):  ' + json.dumps(["apple", "bananas"]))
    print('json.dumps(("apple", "bananas")):  ' + json.dumps(("apple", "bananas")))
    print('json.dumps("hello"):  ' + json.dumps("hello"))
    #print('json.dumps(42):  ' + json.dumps(42))
    print('json.dumps(31.76):  ' + json.dumps(31.76))
    print('json.dumps(True):  ' + json.dumps(True))
    #print('json.dumps(False):  ' + json.dumps(False))
    print('json.dumps(None):  ' + json.dumps(None))

    # Formatting
    print(json.dumps({"name": "John", "age": 30}, indent=2, sort_keys=True))

    # Python	JSON
    # dict	    Object
    # list	    Array
    # tuple	    Array
    # str	    String
    # int	    Number
    # float	    Number
    # True	    true
    # False	    false
    # None	    null
