### Motion Matching 的方法

#### 介绍
[知乎参考](https://zhuanlan.zhihu.com/p/50141261)

起源：Motion Fields，大致思路是根据玩家反馈和当前帧状态搜索动画数据库中最佳匹配的帧或者动画片段，进行合成。
首次提出motion matching，荣耀战魂（UBI）

如何找到与当前动画最匹配的动画数据？
通过对比当前动画与动画数据库中的动画数据的 轨迹，Pose, 速度.

- 轨迹：
首先根据玩家当前的操作输入，结合当前角色运动的**速度，加速度**，可以预判t时间后的角色的**位置**。
随后遍历动画库中每条动画，第0帧开始，逐次对比t秒后的角色位置, 与预判的角色位置做比较，并记录位置间的距离和root朝向。

- Pose
其次，对比当前角色骨骼和片段A的第0帧的角色各骨骼位置，并记录距离的差值。

- 速度
然后对比各个骨骼点的速度，并记录速度的差值。

综合以上规律，搜索到的差越小则表示当前动画帧与搜索出的帧越相近。但是，并不是所有维度都重要，比如位置和骨骼的重要性，不同骨骼之间的差异性等。这时候就需要
分配权重。

[UBI分享](https://montreal.ubisoft.com/en/introducing-learned-motion-matching/)

动画数据库的建立

因为需要搜索大量的动画帧，因此动画数据库中的动作的丰富度应当尽量大。

UBI分享了他们制作时的经验：Dance Card就像是动捕中的单词卡，能够尽量的汇总这些单词，从而组织出动画的语言。

在实际中动画不需要零碎，数据库中的动画都是大段的。

搜索后，得到的数据就是一系列关于某个具体时间上的切片，关键在于如何决定播放开始的时间，通常是手动选择一些特征。根据UBI的分享
脚的位置，速度，角色的腰部速度，还有其未来时间上轨迹的位置和朝向是比较重要的。

(With some experimentation, we can find that the feet positions, their velocities, the character’s hip velocity, and a couple of snapshots from the future trajectory position and direction are the only features we need to achieve this path following task. )

将这些信息组织起来形成一个feature vector，通过对动画数据库里面的数据进行特征提取，将他们存在一个大的特征矩阵中，用于后期查询使用。
对于两个动画之间切换的不连续性，如果前后差异比较小，则会使用动画过渡技术进行弥补(inertialization),这是一种依靠线性插值，惯性插值等方式使得动画之间得以流畅播放的技术,[具体可以参考这里](https://zhuanlan.zhihu.com/p/370019871)

同时还可以对角色使用IK和Foot Locking的方法进一步纠正位置信息。

但是Motion Matching存在的问题是，database比较庞大，查询起来相当的麻烦。所以可以通过训练一个神经网络(Decompressor)的形式，来生成出一些想要的帧。UBI用auto-encoder搭建了一个网络，省去了储存dataset的空间，由网络直接生成，在不降低动画品质的情况下缩小了储存空间一半多。同时为了解决前后帧之间的融合问题，UBI用了Stepper网络去估计融合特征，最终提高了10倍的性能[Paper](https://static-wordpress.akamaized.net/montreal.ubisoft.com/wp-content/uploads/2020/07/09154101/Learned_Motion_Matching.pdf)


- [UNITY的一个实现上述的思路](https://github.com/nashnie/MotionMatching)
- [UNreal中的一个实现](https://github.com/Hethger/UE4_MotionMatching-)


