from itertools import permutations
import string
  
a = 'a', 'b', 'c'
b = string.ascii_letters
c = permutations(a)
  
d = []
for i in list(c):
  
    
    if (i not in d):
        d.append(i)
        print(''.join(i))