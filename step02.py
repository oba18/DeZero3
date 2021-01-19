"""
step02 変数を生み出す関数
"""

import numpy as np
from step01 import *

# 関数の定義
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x ** 2

# test
#  x = Variable(np.array(10))
#  f = Square()
#  y = f(x)
#  print (type(y))
#  print (y.data)

