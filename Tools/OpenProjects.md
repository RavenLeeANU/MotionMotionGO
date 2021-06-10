### OpenMP

OpenMP仅通过线程来完成并行
-	一个线程的运行是可由操作系统调用的最小处理单
-	线程们存在于单个进程的资源中，没有了这个进程，线程也不存在了
-	通常，线程数与机器的处理器/核数相匹配，然而，实际使用取决与应用程序
-	openMP的最大缺点就是非常依赖于编译器版本和链接参数。完全本地开发本地运行的话还没什么问题，一旦需要跨平台，哪怕只是gcc4.7和4.8这样的版本差异带来的c++标准和openmp版本的微小差异，也都有可能出问题

### ML on Web

onnxjs 
official [here](https://github.com/microsoft/onnxjs) [include examples]
demo [here](https://github.com/Microsoft/onnxjs-demo) 

Tensorflow JS
[TFJS](https://github.com/tensorflow/tfjs)
Keras -> TFJS MODEL

### 数据
#### YAML
[参考格式](https://www.runoob.com/w3cnote/yaml-intro.html)
“-” 符号表示数组
“:” 表示名称和值的映射，中间用空格空开
缩进表示所属关系
值可以为空

#### Protobuf
序列化数据存储协议，谷歌搞的，效率比json高3-5倍。
优点：通过以上的时间效率和空间效率，可以看出protobuf的空间效率是JSON的2-5倍，时间效率要高，对于数据大小敏感，传输效率高的模块可以采用protobuf库
缺点：消息结构可读性不高，序列化后的字节序列为二进制序列不能简单的分析有效性；目前使用不广泛，只支持java,C++和Python；

#### XML & JSON
[比较XML，JSON，YAML](https://zhuanlan.zhihu.com/p/79290261)
XML：<label></label>结构
JSON：{“label”:[value1,value2]}结构
