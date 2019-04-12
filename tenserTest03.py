import tensorflow as tf

#텐서플로에서 사용할 상수(변하지 않는값)을 선언
#a는 120이외의 다른값을 가질 수 없어요
#  final int a = 120        자바문법의 이것과 같은 개념
#       ** 자바에서 final이 어디어디 올수 있나요?
#           1. 변수앞에                  ==> 상수
#           2. 메소드앞에                ==> 재정의(오버라이딩)금지
#           3. 클래스앞에                ==> 상속(확장)금지

a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")


#텐서에서 사용할 변수를 선언해요
v = tf.Variable(0, name='v')


#텐서에서 사용할 수식을 만들어요
calc_op = a + b + c
'''
    위의 수식을 위해서는 몇번의 연산이 일어날까요?
    
    a
      +     r
    b
              +   calc_op 
            c
           
    위와 같은 모양을 그래프라고 합니다.
    위와 같은 수식을 만나면 텐서는 이러한 그래프를 생성합니다.
    ==> 그래서 "데이터 플로우 그래프"라고 합니다.               
'''



#위의 수식의 결과(calc_op)를 텐서변수 v에 대입해요
#       아직까지 계산 안한 상태이구요
#       나는 이러이러한 계산을 할꺼야 하고 계획하는 단계입니다.
#           실제계산은 텐서의 Session을 얻고
#           그 session을 run을 만나야 실제 계산이 이루어 집니다.


assign_op = tf.assign(v, calc_op)


#텐서의 수식(assing_op)를 실행시키기 위하여
#텐서의 session이 필요해요

sess = tf.Session()
 # sess.run(assign_op)         #연산한 결과를 텐서변수 v에 담아요
print(sess.run(assign_op))

# print(assign_op)
# print(v)

#v에 담긴 내용를 실행하여 출력합니다.
print(sess.run(v))











































