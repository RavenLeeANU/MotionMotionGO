### 常考题

[参考](https://www.jianshu.com/p/da75f0ac046e)
protected: 在继承或间接继承与这个类的子类中可以访问。
internal：表示对所修饰的成员在当前程序集内可以进行没有任何限制的访问
sealed:能够阻止某一个类被其他类继承
const和readonly有什么区别
Struct属于值类型,是分配在内存的栈上的
内存回收：将线程挂起→确定roots→创建reachable objects graph→对象回收→heap压缩→指针修复。
CTS：通用语言系统。CLS：通用语言规范。CLR：公共语言运行库
应用程序域可以理解为一种轻量级进程。起到安全的作用。占用资源小

### 字符串处理
格式化字符串
string.Format(“{0},{1}”,var1,var2);
–	左侧padding “0”
stringName.ToString().PadLeft(2,'0');

### C#的代码规范相关
[规范相关的博客](https://www.cnblogs.com/wulinfeng/archive/2012/08/31/2664720.html)
–	变量命名：驼峰写法，首字母小写
–	函数命名：驼峰写法，首字母大写
