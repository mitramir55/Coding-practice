import regex as re
pin = 'a234'
a = re.match('^\d+$', pin)
a
re.findall('^\d+$', pin)


out = True if (len(pin)==4 or len(pin)==6) and re.match('^\d+$', pin) else False

out = True if re.match('^\d+$', pin) else False
out

pin.count(r'\d')
re.findall('\d', pin)
import numpy as np
haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
np.where(haystack=='needle')

3//2
'test'[1:-1]
4-1// 
type(3//2)
