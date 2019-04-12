import numpy as np
import tensorflow as tf

student = [
                ['김경민',80,90,100],
                ['강감찬',100,70,100],
                ['이순신',40,80,30],
                ['유관순',100,70,80],
                ['문재인',40,100,90]
           ]


# placeHolder를 이용하여 각 학생의
# 평균을 구하여 출력해 봅니다.

#학생의 점수를 담을 3개짜리 배열을 placeHolder로 만들어요
# ph_score = tf.placeholder(tf.int32, [3])
ph_score = tf.placeholder(tf.float64, [3])

#placeHolder
#===> 값이 들어갈 빈공간을 만드는 개념!

#그 공간을 갖고 미리 계산식을 만들어요.

#placeholder와 Varibale을 무엇이 다른가요??
#정해지지 않은 값이 1개==> Variable
#정해지지 않는 값이 여러개 덩어리==> placeHoler

#name
#insert into member values('"+name+"', )
#insert into member values(?,?,?,?,?)

# 김경민 90
# 강감찬 90
# 이순신 50
# 유관순 83
# 문재인 76

# 김경민 90.0
# 강감찬 90.0
# 이순신 50.0
# 유관순 83.33333333333333
# 문재인 76.66666666666666

#평균을 위한 수식을 만들어요
cnt = tf.constant(3)
# avg =(ph_score[0] + ph_score[1] + ph_score[2])/cnt
# avg = ph_score.mean()             불법
# avg = np.array( ph_score).mean()  불법
# 텐서가 제공하는 평균함수를 이용해요
avg = tf.reduce_mean(ph_score)


#텐서를 실행시키기 위한 session을 얻어 옵니다.
sess = tf.Session()


#학생의 데이터 수 만큼 반복수행하여 run을 시켜요
for row in student:
    name, s = row[0], row[1:]
    r = sess.run(avg, feed_dict={ph_score:s})
    print(name,r)

sess.close()




















