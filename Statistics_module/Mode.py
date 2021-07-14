def mode(mode_list):
    try:
        y = mode_list
        y.sort()
        L1 = []
        i = 0
        while i < len(y):
            L1.append(y.count(y[i]))
            i += 1

        d1 = dict(zip(y, L1))
        d2 = {k for (k, v) in d1.items() if v == max(L1)}

        return d2
    except IndexError or ValueError:
        # Index Error : throws exception if the list is empty
        # Value Error : throws exception if the list contains string values
        return None
