### Inverse Kinematics


IK 即已知终端位置，求各个关节状态。
假设所有杆的长度已知，杆之间组成chain，即骨骼不会发生形变。只有角度会发生变化。

[参考](http://www.3dkingdoms.com/ik.htm#ikstart)

![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/skeleton.png)

IK求解方法
#### 1.直接几何求解
根据链接关系和角度直接暴力解算
缺点：算量大，算式不具备通用性。有可能接出来出现多个解（自由度冗余）或者无解。
FABRIK（ Forward And Backward Reaching Inverse Kinematics）
根据到终端的距离，逐层调整骨骼的位置和距离。
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/fabrik.png)

优点：解的快
[具体参考](https://blog.csdn.net/noahzuo/article/details/80188366)

![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/fabrik-algo.png)
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/fabrik.jpg)


FABRIK还有一个有点是多端约束比较容易实现。
针对于雅可比矩阵操作，FABRIK最终产生的效果不一定比雅可比矩阵更好，但是计算量大大减少。

#### 2.CCD逼近求解Cyclic Coordinate Descent (CCD) 
每次让骨骼的终端与当前的骨骼向量方向连城与目标和当前运算的骨骼方向相同。
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/ccd.png)
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/ccd-step.png)
#### 3.雅可比矩阵求解
将问题转化为优化问题进行求解
参考 https://blog.csdn.net/noahzuo/article/details/54314112
https://zhuanlan.zhihu.com/p/69215035

雅可比矩阵：可以理解为瞬时状态下各个分量的速度投影
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/jacob.png)
一小段y就是x一小段x及其投影。
复习：导数反映的是斜率，对于曲线或者曲面来说，实际上是约束，所以已知n-1维度的值，就可以求出第n维的值，而偏微分就是待求的那一维与第i维的投影。
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/jacob1.png)
平面在空间上有n-1维个偏导数。斜率反映了对应点上 值和这一维的关系，导数越大说明这一维度上的速度越大。
![sk](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Images/jacob2.png)
将其换算成物理量速度的话，可以理解维主速度在分方向的分解对于目标的贡献。
针对于n关节的骨骼架构，雅可比矩阵应该是6*n的形式。
空间解雅可比矩阵，需要计算出贾克比矩阵的约束式，且不同数量关节的约束式也不一样
优点：效果好。缺点：实时性比较差。处理约束和多终端比较麻烦。
https://zhuanlan.zhihu.com/p/69215035
