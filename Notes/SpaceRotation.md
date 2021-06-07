## 空间旋转的数学表达
[参考](https://blog.csdn.net/rubikboy/article/details/104662747)


### 欧拉角

按照x,y,z的三个轴的旋转进行定义，包括偏航（yaw）、俯仰 (pitch) 和滚动 (roll) 三个分量按照一定的顺序进行旋转的**过程**。

![alt text](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/pitch.png)

欧拉角表示法存在的问题是【万向节的死锁】


简要描述就是在某一维度旋转到90度的时候，最终的结果和这一维度就没有关系了。少了一维信息，就像被锁住了。

[参考](https://zhuanlan.zhihu.com/p/346718090)

理解这个问题的关键在于：欧拉角是由三个角度表示，表示物体从原始姿态到目标姿态的一个变换。无论（α，β，γ）三个角度值是多少，都是得从物体的原始姿态开始进行绕轴进行旋转。所以物体的姿态都是相对于其最原始姿态的，上述图例中说到的，先绕X轴旋转30度，再绕Y轴旋转90度，再绕Z轴旋转10度得到的最终姿态和先绕X轴旋转20度，再绕Y轴旋转90度的结果一样。因此相对于最初姿态而言，当一个欧拉角包含绕Y轴旋转90度时，绕X轴和绕Z轴旋转已经是在绕同一个轴在进行旋转，这个时候只有两个轴在起作用。这个时候就是万向锁的状态。

万象锁麻烦的问题在于，在特定的拆分下，得到的三个方向的不唯一。


### 四元数

[参考](https://www.3dgep.com/understanding-quaternions/#Introduction)

四元数顾名思义，就是使用四个维度来表示一个空间角的旋转。使用Hamilton算子来表示为:

![alt text](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/quar.png)

#### 四元数如何表示旋转
使用四元数乘积可以表示旋转或者伸缩，即在一个高维度的空间来表示三维的旋转。实际计算的时候使用 一组共轭的四元数来限制输入和输出的维度一致。

四元数的优点是适合插值，且不会出现被锁死的情况。与角的关系如下：
P’ = Q P Q-1 
其中Q对应旋转的轴向及旋转角度 P表示待旋转的点的位置，具体可以参考。
[参考](https://www.zhihu.com/topic/19594299/hot)

#### 相关四元数的可视化介绍
[参考](https://eater.net/quaternions/video/doublecover)
旋转的时候两个维度在变换，另外一个维度不变，那就是围绕着不变的轴在旋转


### 罗德里格斯公式
[参考](https://blog.csdn.net/q583956932/article/details/78933245)
