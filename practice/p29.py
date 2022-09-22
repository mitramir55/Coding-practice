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
