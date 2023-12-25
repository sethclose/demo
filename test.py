def update_default(dict_1, dict_2):
    for key, value in dict_1.items():
        print(str(key) + " " + str(value))
    for key, value in dict_2.items():
        print(str(key) + " " + str(value))     
        dict_1.setdefault(key,value)
print("")

dict_1 = {"a": 1}
update_default(dict_1, {"a": 2, "b": 3})
print("dict_1 = " + str(dict_1))
#assert dict_1 == {"a": 1, "b": 3}

dict_2 = {"a": 1, "b": 2, "c": 3}
update_default(dict_2, {"a": 4, "e": 5, "f": 6})
print("dict_2 = " + str(dict_2))
#assert dict_2 == {"a": 1, "b": 2, "c": 3, "e": 5, "f": 6}