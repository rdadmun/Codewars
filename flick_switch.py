def flick_switch(lst):
    result = True
    result_lst = []
    for str in lst:
        if str == "flick":
            result = not result
        result_lst.append(result)
    return result_lst