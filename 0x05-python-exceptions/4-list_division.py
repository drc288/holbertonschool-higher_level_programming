#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    new_list = []
    for i in range(list_length):
        flag = False
        try:
            result = my_list_1[i] / my_list_2[i]
            flag = True
        except TypeError:
            print("wrong type")
            new_list.extend([0])
        except ZeroDivisionError:
            print("division by 0")
            new_list.extend([0])
        except IndexError:
            print("out of range")
            new_list.extend([0])
        finally:
            if flag == True:
                new_list.extend([result])
    return new_list
