sentence = "is2 Thi1s T4est 3a" 
import regex as re
dict_ = {}
for word in sentence.split(" "):
    order = re.findall('\d', word)[0]
    dict_[word] = int(order)

type(dict_['is2'])

sorted_list = sorted(dict_.items(), key=lambda x: x[1])

[k for k, v in sorted_list]

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

sorted(sentence.split(), key=lambda w: sorted(w))

word = 'this'
''.join(list(word)[::-1])


text = "double  spaces" 
spaces = re.findall('\s+', text)

reversed_words = [''.join(list(word)[::-1]) for word in text.split()]

for i in range(len(text.split())):
  ret_str = reversed_words[i]

  if i<len(spaces):
    ret_str += spaces[i]



[1,-2,3,-4,5] * [-1]

all_directions= [['NORTH', 'SOUTH'], ['WEST', 'EAST']]
    
arr_str = 'NORTHSOUTH'

patterns_count = 0
for dirs in all_directions:
  if re.findall(dirs[0]+dirs[1], arr_str): patterns_count+=1
  if re.findall(dirs[1]+dirs[0], arr_str): patterns_count+=1


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


str_ = 'AAAABBBCCDAABBB'
list_str = list(str_)
list_str
delete_idx = []

for i in range(len(str_)-1):
  if list_str[i] == list_str[i+1]: 
    print(i+1)
    delete_idx.append(i+1)

delete_idx.reverse()

for i in delete_idx.reverse():
  print(i)
  del list_str[i]

list_str
set(str_)