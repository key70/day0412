import tensorflow as tf


a = tf.constant(2)      #a는 2이외의 다른값을 가질수 없어요!      ==> 상수만들기
b = tf.constant(3)
c = tf.constant(4)

calc1_op = a + b * c

# print(calc1_op)     #Tensor("add:0", shape=(), dtype=int32)
                    #텐서의 상수나 변수 수식의 결과를 바로 이와같아 알아볼 수 없어요
                    #텐서의 실행환경에서 실행시키고 그 결괄르 확인할 수 있어요.

calc2_op = (a+b) * c

sess = tf.Session()
r1 = sess.run(calc1_op)
r2 = sess.run(calc2_op)

print(r1)
print(r2)

