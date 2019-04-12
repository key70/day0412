# 크기가 상관없는 정수형 1차원 배열의 placeHolder 만들고
#   이것의 *2 한 결과를 tensor를 이용하여 출력해 봅시다.

import tensorflow as tf

# 크기가 정해지지 않은 1차원 배열의 placeHolder를 만들어요
arr = tf.placeholder(tf.int32,[None])

# arr의 *2한 수식을 만들어요
# result = arr * 2
# 2를 직접 표현하지 말고 tensor의 상수로 만들어요

n = tf.constant(2)

# 위의 상수를 이용하여 수식을 만들어요
result = arr * n


# session을 얻어와 위의 수식을 실행시켜요
# 실행시킬때는 placeHolder의 값을 지정해야 해요
sess = tf.Session()
r1 = sess.run(result, feed_dict={arr:[1,2]})
r2 = sess.run(result, feed_dict={arr:[10,20,30,40,50]})
x = [7,8,9]
r3 = sess.run(result, feed_dict={arr:x})

print(r1)
print(r2)
print(r3)




