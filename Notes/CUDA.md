### GPU线程

异构：CPU+GPU：通常，我们将在 CPU上执行的代码称为主机代码, 而将在GPU上运行的代码称为设备代码.

初识GPU

[一个不错的系列](https://www.jianshu.com/p/6c4ec3490559)
GPU的架构：
–	ALU(Arithmetic&logical Unit)：算数逻辑单元,由与或门构成
–	DRAM(Dynamic Random Access Memory) 指动态随机存取存储器,DRAM中的数据会在电力切断以后很快消失。
–	控制单元
PS：和CPU的区别是少了三级缓存，分支预测等。ALU的数量增加，上下文存储池被扩大。

PS：上下文存储池分成4份, 也就是说, 可以执行4条指令流, 比方说指令1阻塞, 立马切换指令2, 指令2阻塞切换指令3, 这就起到了隐藏延迟的效果. 当然数量到底是多少是很讲究的, 不是越多越好.

一个GPU内核：含8个ALU, 4组执行环境(Execution context), 每组有8个Ctx. 这样, 一个这样的内核可以并发(concurrent but interleaved)执行4条指令流(instruction streams), 32个并发程序片元(fragment).
GPU线程：在CUDA架构下, 显示芯片执行时的最小单位是thread. 数个thread可以组成一个block. 一个block中的thread能存取同一块共享的内存(shared memory), 而且可以快速进行同步的动作, 特别要注意, 这是块(block)同步.不同block中的thread无法存取同一个共享的内存, 因此无法直接互通或进行同步. 因此, 不同block中的thread能合作的程度是比较低的.
