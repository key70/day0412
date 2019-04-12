# placeHoder란?
#   마치 데이터베이스의 PrepareStatement 처름
#       질의문의 ?를 생각하면 될 것 같아요
#      사용자가 입력한 값을 질의문에 대응시키기 위하여 ?를 대신하듯이

# 어떤 수식에 대응시키기 위한 변수의 틀을 미리 만들어 두는 개념입니다.
# 예를 들의 다음의 수식을 볼까요?
#  a = [1,2,3]
#  b = a * 2
#  b는 정해진 배열 [1,2,3] * 2 만 할줄알아요.
#       만약, 어떤요소의 배열이라도 연산시키고자 한다면
#       위와 같이 값을 구체화 하지 않고
#   다만, 3개짜리 배열이야 라고만 틀을 만들어 두면
#           어떤 요소의 배열이라도 연산시킬수 있어요

import tensorflow as tf


# 어떤 값이라도 담을수 있는 정수형 3개를 담을 수 있는 placeHolder를 만들어요
# 그 placeHolder 이름을 a라고 합시다.
a = tf.placeholder(tf.int32,[3])


# 위에서 만든 placeHolder가 사용되는 수식(데이터 플로우 그래프)을 만들어 봅시다.
b = tf.constant(2)
x_op = a * b


#위의 수식을 실행시켜 봅시다.
#실행시키려면 먼저 tensor의 session을 얻어와요 해요

sess = tf.Session()


#위의 수식 x_op를 실행시키려고 합니다.
#위의 수식 x_op에는 결정되지 않는 값(즉 placeHolder)를 갖고 있기 때문에
#실행시에 반드시 placeHoler의 값을 설정해 줘야 해요!
r1 = sess.run(x_op, feed_dict={a:[1,2,3]})
print(r1)


r2 = sess.run(x_op, feed_dict={a:[4,5,6]})
print(r2)


row = [10,20,30]
r3 = sess.run(x_op, feed_dict={a:row})
print(r3)












