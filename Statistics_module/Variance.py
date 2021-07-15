import statistics


def variance(variance_list):
    try:
        var = statistics.variance(variance_list)
#        std_list = sum(variance_list) / len(variance_list)
#        var = sum(pow(x-std_list, 2) for x in variance_list) / len(variance_list)
        return var
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
