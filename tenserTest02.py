#!/usr/bin/env python
# coding: utf-8

# # 주피터노트북에서 Tensorflow 사용하기
# - 주피터 노트북에서 tensorflow 코드를 실험해 봅시다.

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# In[4]:


import pandas as pd


# In[5]:


import tensorflow as tf


# In[7]:


# constant ===> 상수만들기
a = tf.constant(100)
b = tf.constant(50)
add_op=a+b

# Variable    ==> 변수만들기
v = tf.Variable(0)

#add_op의 연산결과를 텐서변수 v에 대입하려고 한다.
let_op = tf.assign(v, add_op)


# In[8]:



#텐서를 실행시키기 위한 session을 생성
sess = tf.Session()

#텐서의 변수(Variable)를 사용하기 위해서는 반드시 초기화 과정을 거쳐야 해요.
sess.run(tf.global_variables_initializer())

#let_op 에 지정한 수식을 실행시켜요
sess.run(let_op)

#연산결과가 담긴 텐서 Varibale v의 내용을 출력해요
print(sess.run(v))


# In[ ]:




