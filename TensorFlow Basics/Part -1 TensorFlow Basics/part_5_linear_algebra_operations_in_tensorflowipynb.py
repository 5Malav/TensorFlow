# -*- coding: utf-8 -*-
"""Part-5 Linear Algebra Operations in TensorFlowipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JwNMIvTSZ_parI3eNQiNwWXyJKsu2v3U
"""

import tensorflow as tf

# tf. linalg. matmul

# Mutliplication matrix a by matrix b producing a*b

# when we multiply matrix
# No. of columns of 1st matrix should always match the number
# of rows of the second matrix.

a = tf.constant([
    [3,1,9,6,5],
    [0,1,7,3,2],
    [1,5,1,2,0],
    [7,3,0,9,0]
])


b = tf.constant([
    [3,1,9,6,5],
    [0,1,7,3,2],
    [1,5,1,2,0],
    [7,3,0,9,0],
    [1,4,5,9,10]
])

tensor_matrix = tf.linalg.matmul(
    a,
    b,
    transpose_a=False,
    transpose_b=False,
    adjoint_a=False,
    adjoint_b=False,
    a_is_sparse=False,
    b_is_sparse=False,
    output_type=None,
    name=None
)
print(tensor_matrix)

a = tf.constant([
   [1,2,3],
   [4,5,6]
])


b = tf.constant([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

tensor_matrix = tf.linalg.matmul(
    a,
    b,
    transpose_a=False,
    transpose_b=False,
    adjoint_a=False,
    adjoint_b=False,
    a_is_sparse=False,
    b_is_sparse=False,
    output_type=None,
    name=None
)
print(tensor_matrix)

a = tf.constant([
   [1,2,3],
   [4,5,6]
])

print(a)

print("")

print(a.shape,tf.transpose(a))

# a * transpose(b)


a = tf.constant([
   [1,2,3],
   [2,1,1]
])


b = tf.constant([
    [1,2,3],
    [4,5,6],
    [2,2,2]
])

print(a)
print(" ")

print(b.shape,tf.transpose(b))

print(" ")

tensor_matrix = tf.linalg.matmul(
    a,
    b,
    transpose_a=False,
    transpose_b=True,
    adjoint_a=False,
    adjoint_b=False,
    a_is_sparse=False,
    b_is_sparse=False,
    output_type=None,
    name=None
)
print(tensor_matrix)

a_three_d = tf.constant(
    [
      [[1,2],
      [3,5]],

      [[10,2],
       [1,0]],

      [[5,8],
       [2,7]],

      [[2,1],
       [4,3]]
        ]
)
print(a_three_d)

b_three_d = tf.constant(
    [
      [[1,2,0],
      [3,5,-1]],

      [[10,2,0],
       [1,0,2]],

      [[5,8,8],
       [2,7,0]],

      [[2,1,9],
       [4,3,-2]]
        ]
)
print(b_three_d)

print(a_three_d.shape,b_three_d.shape)

print(tf.linalg.matmul(a_three_d,b_three_d))

print(a_three_d[0],b_three_d[0])

a_three_d[0]@b_three_d[0]

a_three_d[2]@b_three_d[2]

# tf. linalg.band_part

# Copy a tensor setting everything outside a central band in each
# innermost matrix to zero

x =  tf.constant([[0,1,2,3],
                  [-1,0,1,2],
                  [-2,-1,0,1],
                  [-3,-2,-1,0]])
x

a =  tf.constant([
    [1,5,1],
    [7,9,3],
    [1,3,1]
    ])
a

"""
Condition:- m for row and n for column

m = 0, n = 0, m-n =0, n-m =0

False             True                 False          True
        True                                    True
                                True
(num_lower<0 || (m-n)<=num_lower) && (num_upper<0 || (n-m)<=num_upper)

"""

tensor_band_part=tf.linalg.band_part(a,0,0)
print(tensor_band_part)

# tf. linalg. det

# Computes the determinant of one or more square matrices

# No of rows should be equal to No. of columns

x =  tf.constant([[1.0,2.0],
                  [5.0,6.0]])

y =  tf.constant([[1.0,2.0],
                  [3.0,4.0]])

tensor_deter= tf.linalg.det(x,y)
tensor_deter

# Inverse of a matrix

# A inverse* A = Identity matrix

# tf.linalg.inv

# Cmputes the inverse of one or more square matrices or their
# adjoints( conjuagate transposes)

x =  tf.constant([[1.0,2.0],
                  [5.0,6.0]])

y =  tf.constant([[1.0,2.0],
                  [3.0,4.0]])

tf.linalg.inv(x,adjoint=True)

# tf. einsum

# Tensor contraction over specified indices and outer product

a = tf.constant([[1,2,],
               [3,4]])

b = tf.constant([[1,2,],
               [3,4]])

tf.linalg.matmul(a,b)

tf.einsum("ij,jk->ik",a,b)

a =  tf.constant([2,6,5,2])
b = tf.constant([0,1,3,2])

tf.einsum("i,j->",a,b)

tf.einsum("i,j->ji",a,b)

tf.einsum("i,i->",a,b)

tf.einsum("j,j->",a,b)