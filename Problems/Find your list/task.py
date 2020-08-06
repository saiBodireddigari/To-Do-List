def find_my_list(all_lists_, my_list):
    for index_, lst in enumerate(all_lists_):
        # Change the next line
        if id(my_list) == id(lst):
            return index_
    return None
