# -*- coding: utf-8 -*-
"""Copy of Partial derivatives and gradients exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EFX9IxAtNgCkyBrDHLw3I62Q9S_njzDC

# נגזרות חלקיות וגרדינט

תרגיל 6 שקף 6
"""

import numpy as np

"""![image.png](data:image/png;base64,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)"""

def df_dx1(x1, x2):
  return 2*x1 + x2

def df_dx2(x1, x2):
  return x1 + 4*x2

"""תרגיל 7 שקף 7"""



"""![image.png](data:image/png;base64,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)"""

def df1_dx(x, y):
  return 2*x + 3*y

def df1_dy(x, y):
  return 3*x + 2*y

def gradient_f1(x,y):
  return np.array([df1_dx(x,y) , df1_dy(x,y)])

gradient_f1(-2,5)

gradient_f1(-2,5)

"""![image.png](data:image/png;base64,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)"""

def df2_dx(x, y):
  return 2*x + 6*y*x

def df2_dy(x, y):
  return 3*x*x + 3*y*y

def gradient_f2(x,y):
  return np.array([df2_dx(x,y) , df2_dy(x,y)])

gradient_f2(3,-2)

gradient_f2(3,-2)

"""![image.png](data:image/png;base64,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)"""

def df3_dx(x, y, z):
  return 5 + 2*y*y

def df3_dy(x, y, z):
  return 4*x*y + 3*z*z

def df3_dz(x,y,z):
  return 6*y*z

def gradient_f3(x,y, z):
  return np.array([df3_dx(x,y,z) , df3_dy(x,y,z) , df3_dz(x,y,z)])

gradient_f3(-5,7,3)

gradient_f3(-5,7,3)