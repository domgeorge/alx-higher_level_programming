#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ini = 0
    ini1 = 0
    for i in my_list:
        ini += i[0] * i[1]
        ini1 += i[1]
    return (ini / ini1)
