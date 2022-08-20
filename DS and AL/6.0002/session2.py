# Import the os module
import os
import time
# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
os.chdir(r'C:\Users\mitra\Coding-practice\DS and AL\6.0002')

os.getcwd()


from session1 import Food, build_menu, test_greedys, test_greedy 

def max_available(items, available_space):

    # nothing else to consider OR no available weight
    if available_space == 0 or items == []:

        # space and items available
        result = (0, [])

    # there is no way we can take item[0]
    elif items[0].get_cost() > available_space:
        result = max_available(items=items[1:], available_space=available_space)
    
    # it might be good for us to take it
    else:

        # what if we take it?
        with_item_value, with_items = max_available(items[1:], available_space-items[0].get_cost())
        
        # add the value to the whole value
        with_item_value += items[0].get_value()

        # what if we didn't?
        without_item_value, without_items = max_available(items[1:], available_space)

        # which?
        if with_item_value > without_item_value:
            print(items[0])
            result = (with_item_value, with_items + [items[0]])
        else:
            result = (without_item_value, without_items)
    return result

def test_max_value(items, max_units):

    print('maximum is ', max_units)

    value, items_picked = max_available(items, available_space=max_units)
    print('the final value is {value} and the items are:')
    for item in items_picked: print(item.name)
    print('value reached to ', value)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
menu = build_menu(names, values, calories)





test_greedys(menu, 750)

test_max_value(menu, 750)



# fibo in its real sense


def fast_fibo(n, memo={}):

    if n ==0 or n==1:
        return 1
    else: 
        try: memo[n]
        except:
            new_num = fast_fibo(n-1, memo) + fast_fibo(n-2, memo)
            memo[n] = new_num
            return new_num


def max_val_f(left_items, remaining_val, memo={}):

    # why? can't this be different? with different items
    if left_items == [] or remaining_val == 0:
        result = (0, [])

    elif (len(left_items), remaining_val) in memo:
        result = memo[(len(left_items), remaining_val)]

    elif left_items[0].get_value() > remaining_val:
        result = max_val_f(left_items[1:], remaining_val)

    else:
        # why don't we use memo on top of this? in the else?
        with_item_val, with_item_items = max_val_f(left_items[1:], 
        remaining_val=remaining_val-left_items[0].get_value(), memo=memo)

        with_item_val += left_items[0].get_value()

        without_item_value, without_item_items = max_val_f(left_items[1:], 
        remaining_val=remaining_val, memo=memo)

        if with_item_val > without_item_value:
            result = (with_item_val, with_item_items + [left_items[0]])

        else: result = (without_item_value, without_item_items)

    memo[(len(left_items), remaining_val)] = result
    return result



def test_fast_max_val(items, max_units, max_func):

    value, items_taken = max_func(items, max_units, memo={})
    print('this is the value = ', value)
    print('these are the items:')
    for item in items_taken:
        print(item)

import random
def build_large_menu(number_of_items, max_val, max_cost):

    for i in range(number_of_items):
        menu.append(Food(random.randint(0, max_val), str(i), random.randint(0, max_cost)))
    return menu
numItems = 50
print('Try a menu with', numItems, 'items')
items_left = build_large_menu(numItems, max_val=90, max_cost=250)

start = time.time()
test_fast_max_val(items_left, max_units=750, max_func=max_val_f)
end = time.time()

print(f'time taken = ', end - start)

start = time.time()
test_max_value(items_left, 750)
end = time.time()


print(f'time taken = ', end - start)