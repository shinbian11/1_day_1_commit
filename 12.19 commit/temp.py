# Linear Regression

# 이 소스파일은 giothub에 hunkim/DeepLearningZeroToAll 의 파일들을 참고했습니다.

'''
H(x) = Wx + b
- reduce_mean :  average 구하는 함수
- square  : 제곱 하는 함수
- GradientDescent~~. minimize : 최소값 구하는 함수

- W와  b는 값을 변경할수 있으므로 variable로 선언

'''
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

'''
- W가 1, b가 0에 수렴할 때 가장 원하는 결과가 나온다
(가장 cost가 작게 나온다)
- W,b,hypothesis,cost를 각각 설계.
- W,b는 어떤 값인지 모르니까 일단 랜덤 값을 대입
'''
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# hypothesis (= H(x))
hypothesis = x_train * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# optimizer(cost의 최솟값을 구해야 하니까)
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    # 2000번 돌리면서 값을 낼건데, 100번에 한번씩 출력도 하기
    for step in range(2001):
        _, cost_val, W_val, b_val = sess.run([train, cost, W, b])

        if step % 100 == 0:
            print(step, cost_val, W_val, b_val)
            
            
            
'''
step      cost         W             b

0 0.8281512 [0.41554114] [0.5063781]
100 0.03645012 [0.7787899] [0.502856]
200 0.02252397 [0.82611054] [0.39529154]
300 0.013918437 [0.8633071] [0.31073508]
400 0.008600746 [0.89254695] [0.24426611]
500 0.005314739 [0.9155321] [0.19201541]
600 0.003284183 [0.9336005] [0.15094155]
700 0.0020294262 [0.9478039] [0.11865383]
800 0.0012540641 [0.9589691] [0.09327281]
900 0.00077493506 [0.967746] [0.07332088]
1000 0.00047886127 [0.97464544] [0.05763679]
1100 0.000295907 [0.9800691] [0.04530784]
1200 0.00018285184 [0.98433244] [0.03561601]
1300 0.000112992384 [0.98768383] [0.02799747]
1400 6.982155e-05 [0.9903185] [0.02200849]
1500 4.314512e-05 [0.99238944] [0.01730058]
1600 2.6661219e-05 [0.9940174] [0.01359984]
1700 1.6474829e-05 [0.99529713] [0.01069073]
1800 1.01806645e-05 [0.9963031] [0.0084039]
1900 6.2912036e-06 [0.9970939] [0.00660626]
2000 3.8874196e-06 [0.99771553] [0.00519314]

> cost는 점점 작아지고, W는 1에, b는 0에 수렴한다.
'''
            
