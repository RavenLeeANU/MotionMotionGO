
[简介](https://www.cnblogs.com/vickylinj/p/13827826.html)
结构：

骨架信息 和 数据块

–	骨架信息：按照层次关系，定义了如root hip leg等位置和旋转分量，从而形成一个完整的骨架
–	数据块：对应上面的骨架各部位标出每帧的数据信息

HIERARCHY

ROOT {ROOT_NAME}

OFFSET  0.00    0.00    0.00 //相对父节点的偏移

CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation //父节点有6channel 子节点可以根据父节点的偏移推算出来

数据块结构：MOTION

数据块记录了每个关节的每帧运动信息

接下来的一长串数字就是实际的运动数据数据块，对应上面定义好的骨架信息层次结构。
（数字的个数=（JOINT个数*JOINT自带的CHANNELS个数+ROOT*ROOT自带的CHANNELS个数）*Frames，本例中：（17*3+6）*2=112）
