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