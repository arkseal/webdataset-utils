def combine_functions(*funcs):
    def wrapper(i):
        for func in funcs:
            i = func(i)
        return i

    return wrapper
