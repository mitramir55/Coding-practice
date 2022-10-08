def is_one_edit_away(s1:str, s2:str) -> bool:
    """
    determines if two strings are different by less than two edits.
    cat -> mat : True
    cat -> matt: False
    """
    if abs(len(s1) - len(s2)) > 1: return False
    char_map = [0] * 128
    for k in s1:
        idx = ord(k)
        char_map[idx] += 1
    for k in s2:
        idx = ord(k)
        char_map[idx] -= 1

    # more than two because we're ok with each having one different letter
    if sum(abs(i) for i in char_map) > 2: return False
    return True

is_one_edit_away('mat', 'catt')




def one_way_equal_lens(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1: return False
    return True

def one_edit_diff_lens(s1, s2):

    # if length wise s2 > s1
    count = i = 0
    while i < len(s1):
        if s2[i + count] == s1[i]:
            i += 1
        else:
            count += 1
            if count > 1: return False
    return True

def is_one_edit_away(s1:str, s2:str) -> bool:

    len_1 = len(s1)
    len_2 = len(s2)

    if abs(len_1 - len_2) > 1: return False

    if len_2 > len_1: return one_edit_diff_lens(s1, s2)
    elif len_2 < len_1: return one_edit_diff_lens(s1, s2)
    else: return one_way_equal_lens(s1, s2)

is_one_edit_away('mat', 'cat')