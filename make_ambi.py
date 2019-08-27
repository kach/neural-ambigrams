import sys

num1 = sys.argv[1].upper()
num2 = sys.argv[2].upper()

import string
key = string.digits + string.ascii_uppercase

for a, b in zip(num1, reversed(num2)):
    print('<img src="emout-reg-hi/out-%s-%s.png"/>' % (key.index(a), key.index(b)), end='')

print('<br/>')
print('<br/>')

for a, b in zip(reversed(num1), num2):
    print('<img src="emout-reg-hi/out-%s-%s.png"/>' % (key.index(b), key.index(a)), end='')
