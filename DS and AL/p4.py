from cgitb import small


# create power sets

def gen_subsets(arr):

    if len(arr) == 0: return [[]]

    # smaller array all subsets except for the last element
    smaller_sets = gen_subsets(arr[:-1])

    # just the last one
    extra = arr[-1:]

    new_set = []
    for smaller_set in smaller_sets:
        new_set.append(smaller_set + extra)

    return smaller_sets + new_set