#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    arr = []
    while n < list_length:
        try:
            r = my_list_1[n] / my_list_2[n]
            arr.append(r)
        except ZeroDivisionError:
            arr.append(0)
            print("division by 0")
        except TypeError:
            arr.append(0)
            print("wrong type")
        except IndexError:
            arr.append(0)
            print("out of range")
        finally:
            n += 1
    return arr
