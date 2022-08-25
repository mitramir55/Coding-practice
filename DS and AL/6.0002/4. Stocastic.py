import random
from secrets import choice
def head_or_tail():
    rand = random.random()
    print(rand)
    return 'head' if rand<0.5 else 'tail'

def simulation_1(heads=5, total=10):
    sum_ = 0
    for _ in range(total):
        res = head_or_tail()
        if res=='head': sum_ += 1
    
    return (sum_/total)


simulation_1(1, 20)

def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])

# num_trial times role the dice len(goal) times and 
# see how many times
# you get this
def simulation_2(n_trials, n_dice_rols=5, goal='11111'):

    sum_ = 0

    for i in range(n_trials):
        final_s = ''
        for j in range(n_dice_rols):
            res = roll_die()
            final_s += str(res)
        if final_s==goal: sum_ += 1
    return sum_/n_trials

simulation_2(n_trials=10000, n_dice_rols=5, goal='12345')


# same birthday! 🎂 

def same_date(num_people, num_same):
    possbile_dates = range(0,365)

    birthdays = [0]*365
    for _ in range(num_people):
        birthdays[random.choice(possbile_dates)] +=1

    return max(birthdays) >= num_same

same_date(num_people=100, num_same=2)


def same_date_prob(n_trials, num_people, num_same):

    sum_ = 0
    for _ in range(n_trials):
        if same_date(num_people, num_same): sum_+= 1
    return sum_/n_trials

same_date_prob(n_trials=50, num_people=100, num_same=2)
import math
for num_people in [10, 20, 40, 100]:

    est = same_date_prob(10000, num_people, num_same=2)
    print(f'for {num_people} people, the estimated probability is {est}')
    numerator = math.factorial(365)
    denom = math.factorial(365-num_people)*365**num_people

    print(f'And the actual prob is = ', 1- numerator/denom)
    print()