def cal_steps(n):
    memo = {1: 1, 2: 2}
    if n in memo: return memo[n]
    else: 
        memo[n] = cal_steps(n-1) + cal_steps(n-2)
        return memo[n]

def in_order(root):
    ret_list = []
    if root:
        ret_list += in_order(root.left)
        ret_list += [root.val]
        ret_list += in_order(root.right)
    else: return []
    return ret_list


def get_len(root):
    if root:
        return 1 + get_len(root)
    return 0



def get_diameter(root):

    l_right = get_len(root)
    l_left = get_len(root)

    while root.right:
        other_rights = get_diameter(root.right)

    while root.left:
        other_lefts = get_diameter(root.left)

    return max(l_right, l_left, other_rights, other_lefts)