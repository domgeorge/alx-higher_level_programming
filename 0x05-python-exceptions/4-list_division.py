#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divide element by element 2 lists."""
    ele = []
    for u in range(list_length):
        try:
            divi = my_list_1[u] / my_list_2[u]
        except TypeError:
            print("wrong type")
            divi = 0
        except ZeroDivisionError:
            print("division by 0")
            divi = 0
        except IndexError:
            print("out of range")
            divi = 0
        finally:
            ele.append(divi)
    return ele
