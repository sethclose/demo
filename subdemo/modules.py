# Modules
def mods():
    """
    Function for experimenting with modules
    """
    import platform
    for index, func in enumerate(dir(platform)):
        if index == 54:
            print(f"function #{str(index)} is {str(func)} = {platform.python_version()}")   
    return
