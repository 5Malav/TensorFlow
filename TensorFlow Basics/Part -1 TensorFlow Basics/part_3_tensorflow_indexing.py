# -*- coding: utf-8 -*-
"""Part -3 TensorFlow Indexing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U0VVxg6RJBzs3V0sAsIUss9MPEjDvyxT
"""

import tensorflow as tf

tensor_index = tf.constant([2,4,9,0,4,1,3])

# get value 4

print(tensor_index[3])

print(tensor_index[1],tensor_index[-1])

print(tensor_index[0:4])

#start:end


#tensor_index[start:end+1]
print(tensor_index)

tensor_index[0:2+1]

tensor_index[3:5+1]

tensor_index[3:]

tensor_index[3:-1]

tensor_index[2:-2]

tensor_index[:6]

tensor_index[0:5:2]

print(tensor_index[0:5:2])

print(" ")

print(tensor_index[0:5:1])

# 2D tensor

tensor_index_two_d = tf.constant([[1,2,3,4],[6,7,8,9],[10,11,12,14]])

print(tensor_index_two_d)

print(tensor_index_two_d[1])

print(tensor_index_two_d[1,2])

print(tensor_index_two_d[1,2:4])

print(tensor_index_two_d[1,1:4+1])

print(tensor_index_two_d[0:2,0:3])

print(tensor_index_two_d[:,0:3])

print(tensor_index_two_d[:1,0:3])

print(tensor_index_two_d[0,...])# 1D tensor

print(" ")

print(tensor_index_two_d[0:1,...]) # 2D tensor with column and row

print(tensor_index_two_d)

print(" ")

print(print(tensor_index_two_d[0:2,1:3]))

tensor_index_three_d = tf.constant(
    [
      [[1,2,0],
      [3,5,-1]],

      [[4,7,8],
       [9,10,12]],

      [[5,8,8],
       [2,7,0]],

      [[2,1,9],
       [4,3,-2]]
        ]
)
print(tensor_index_three_d)

tensor_index_three_d.shape

print(tensor_index_three_d[3,0,2])

# 3rd block, 0th row, 2nd column

# print 9

print(tensor_index_three_d[3,0,:])

print(tensor_index_three_d[1,1,2])

#print 12

print(tensor_index_three_d[2,:,0:2])