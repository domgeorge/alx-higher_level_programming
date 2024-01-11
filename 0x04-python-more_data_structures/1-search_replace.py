#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == u else u for u in my_list]
