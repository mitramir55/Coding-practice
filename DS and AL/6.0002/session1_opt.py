
# a food object ----------------
class Food:

    def __init__(self, value, name, calories):
        self.value = value
        self.name = name
        self.calories = calories
    
    def get_cost(self):
        return self.calories

    def get_value(self):
        return self.value
    
    def get_density(self):
        return self.value/self.calories

    def __str__(self) -> str:
        return str(self.name) + ' (value = ' + str(self.value) + ', calories ' + str(self.calories) + ')'

"""
burger = Food(value=60, name='burger', calories=100)
burger.__str__()
"""

# a menu for all the foods ----------------
def build_menu(names, values, calories):

    menu = []
    print('names len = ', len(names))
    for i in range(len(names)):
        menu.append(Food(name=names[i], value=values[i], calories=calories[i]))
    return menu
    
"""
names, values, calories = ['ham', 'flower', 'bugs'],\
    [2, 0, 10], [10, 2, 50]

menu = build_menu(names=names, values= values, calories= calories)

menu

"""

#  ----------------

def greedy(items, sort_key_funct, max_cost=60):

    items_sorted = sorted(items, key=sort_key_funct)

    final_list = []
    total_cost = 0
    total_value = 0

    for i in range(len(items_sorted)):
        if total_cost + items_sorted[i].get_cost() < max_cost:
            final_list.append(items_sorted[i])
            
            total_cost += items_sorted[i].get_cost()
            total_value += items_sorted[i].get_value()
            
    return final_list, total_value


def test_greedy(items, sort_key_funct, max_cost=60):
    final_list, total_value = greedy(items, sort_key_funct, max_cost=max_cost)
    print('Total value = ', total_value)
    for i in final_list: print('item: ', i.name)
"""
test_greedy(items=menu, sort_key_funct= lambda x:x.get_cost(), max_cost=max_cost)
"""




# ---------------------------------------
def test_greedys(menu, max_units=60):

    print('use values as a threshold')
    print('value = ', max_units)
    test_greedy(items=menu, sort_key_funct=Food.get_value, max_cost=max_units)


    print('use cost as a threshold' )
    print('cost = ', ' max_units')
    test_greedy(items=menu, sort_key_funct=Food.get_cost, max_cost=max_units)

    print('use a reverse metric for cost (from high to low)')
    print('reverse cost = ', max_units)
    test_greedy(items=menu, sort_key_funct=lambda f:1/f.get_cost(), max_cost=max_units)


    print('use density')
    print('max units = ', max_units)
    test_greedy(items=menu, sort_key_funct=Food.get_density, max_cost=max_units)
"""
test_greedys(max_units=60)
"""