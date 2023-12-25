def errors():
    """
    Function for Experimenting with Errors
    """
    # KeyError Exception
    config = {"count": 3}
    try:
        print("config = {'count': 3}  try: total = config['counter']")
        total = config["counter"]
    except KeyError:
        print("   except KeyError, total = 0")
        total = 0

    # Different Math Types of Exceptions
    catches = []
    try:
        print("catches=[], try: 1/0")
        1 / 0
    except ZeroDivisionError:
        catches.append("Zero division error")
    except ArithmeticError:
        catches.append("Arithmetic error")
    except Exception:
        catches.append("Exception")
    else:
        catches.append("Else")
    finally:
        catches.append("Finally")
    print("Caught Exception(s):" + str(catches))
    return
