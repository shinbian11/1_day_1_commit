# 세션이 없기 때문에 def 함수 선언을 이용하여 값을 더한다.

# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
 
import tensorflow as tf
 
# 앞쪽 레이어의 노드 빌드하기
node1 = tf.constant(9.10, tf.float32)
node2 = tf.constant(0.9, tf.float32)
 
# 뒷쪽 레이어의 노드(즉 node3)를 함수로 정의하기
@tf.function
def forward() :
    return node1 + node2
 
# 그래프를 실행시키고 output을 확인해보기
out_a = forward()
print(out_a)
