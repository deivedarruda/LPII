


"""import time
import os


print(time.asctime())
print(time.timezone)
print(os.name)
print(math.exp(5))"""

import matematica

def test_soma01():
    assert(matematica.soma(5,7)==12)

def test_soma02():
    assert(matematica.soma(1,2)==3)
def test_soma03():
    assert(matematica.subtracao(7,5)==2)