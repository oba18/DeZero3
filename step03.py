"""
step03 関数の連結
"""

import numpy as np
from step02 import *

class Exp(Function):
    def forward(self, x):
        return np.exp(x)

# test
#  A = Square()
#  B = Exp()
#  C = Square()
#
#  x = Variable(np.array(0.5))
#  a = A(x)
#  b = B(a)
#  y = C(b)
#
#  print (y.data)
