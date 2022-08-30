import datetime
str(datetime.timedelta(seconds=666))


intervals = [
    ('year', 60 * 60 * 12 * 365),
    ('day', 60 * 60 * 12),
    ('minute', 60 * 60),
    ('second', 60)
]

5 // 360

def get_plural_s(t):
    return 's' if t > 1 else ''

seconds = 500000
dict_ = {}
plural = False

for inter, val in intervals:
    res = seconds // val

    if res != 0:
        if res > 1: p = get_plural_s(res)
        seconds = seconds % val
        dict_[inter + p] = res



dict_
all_l = []
for k, v in dict_.items():
    all_l += [k, v]

ret_dict = {
    0: 'now',
    1: '{} {}',
    2: '{} {} and {} {}',
    3: '{} {}, {} {} and {} {}',
    4: '{} {}, {} {}, {} {} and {} {}'
}[len(dict_)].format(*all_l[::-1])


ret_dict
all_l

*all_l

all_l
dict_.items()