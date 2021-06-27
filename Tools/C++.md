C++11以后的新特性，C++ STL原理与实现，C++内存管理，C++面向对象编程等。

C++内存管理：
–	C++的构造函数，复制构造函数，和析构函数。什么是深复制和浅复制，构造函数和析构函数哪个能写成虚函数，为什么。
拷贝(复制)构造函数：同一个构造，不同的传入值。

–	动态绑定和静态绑定
对象的静态类型和动态类型：
 静态类型：声明时的类型 比如 ClassA a，那静态类型就是ClassA，对象在声明时采用的类型，在编译期既已确定；
 动态类型：由它实际指向的类型确定，a = new ClassB，那动态类型就是ClassB，通常是指一个指针或引用目前所指对象的类型，是在运行期决定的
静态绑定：绑定的是静态类型，所对应的函数或属性依赖于对象的静态类型，发生在编译期；
动态绑定：绑定的是动态类型，所对应的函数或属性依赖于对象的动态类型，发生在运行期；
那些事静态，那些是动态：非虚函数一般都是静态绑定，而虚函数都是动态绑定（如此才可实现多态性）

–	虚函数和虚表的原理是什么
[参考](https://zhuanlan.zhihu.com/p/98776075)
查虚函数表：虚指针来调用。编译时产生虚函数表。
A强制转换成B之后，理应掉用B，但是无法改变A是A的事实，种调用还是执行A的vfun1
int main() 
{
    B b;
    b.vfunc1();
    A a = (A)b;
    a.vfunc1();
}
改成
int main() 
{
    A* pa = new B;
    pa->vfunc1();
    B b;
    pa = &b;
    pa->vfunc1();
}
之后，pa 是一个类A的指针，但它指向的是一个类B的对象。在使用pa调用 vfunc1 的时候，程序发现pa是一个指针，并且现在正在调用一个虚函数叫做 vfunc1，这时通过 pa->vptr 这个虚指针到类B的虚函数中（上图的B vtbl）找对应的虚函数地址，找到该地址以后，就用相应的虚函数来进行调用，也就是调用上图所示的 B::vfunc1()。

这样就解决了多态产生的混乱。

虚函数的地址存放于虚函数表之中。运行期多态就是通过虚函数和虚函数表实现的。


–	指针的工作原理，函数的传值和传址

–	C++内存区域划如何分说一下（栈，堆那些）


C++11 新特性：
–	auto关键字知道吗，如果全部都用auto声明变量行不行
类似var，可以自动推断。

–	lambda表达式会用吗
(int x, int y) { return x + y; }

–	override关键字必须：
可以编过，但是可能重载不正确。


C++STL
–	STL的六大部件和联系
[参考](https://zhuanlan.zhihu.com/p/147676383)：容器、算法、迭代器、
仿函数：所谓的仿函数(functor)，是通过重载()运算符模拟函数形为的类，比如operator
适配器（配接器）：用来让一个函数对象表现出另外一种类型的函数对象的特征。
1.	绑定器：就是sort(begin,end,XXX)后面那个XXX用来调整值。
空间配置器(allocator):给容器分配内存空间。

–	hashtable的作用与原理
Hashtable 是一个散列表，它存储的内容是键值对(key-value)映射
构造方法：直接定址，除余，根据存储的数据特性分析法等等。
冲突解决：开放地址，线性探测

–	操作符重载问题
哪些符号不可重载：. .* ?: :: # 
重载 Box operator+(const Box& b) {return xxxx}

–	函数模板（泛化和特化的问题),什么是全特化和偏特化
全特化是所有的模板参数都被进行特化，偏特化也就是局部的参数特化。
比如：两个值，都是模版，就是全特化，有一个是int，就是偏特化。调用的时候执行最符合特化的模板。比如<T,T>和<T,int>,其中<double,int>会走后者，<double,double>会走前者。

–	STL中常见的算法用过哪些，原理是什么（随机数，查找等）
<algorithm>中find返回查找元素的索引值，count，search


–	右值引用的应用，优点，lambda表达式（网易客户端，吉比特）
[左值和右值](https://blog.csdn.net/xuwqiang1994/article/details/79924310)：左值，一个在内存中占有确定位置的对象。右值恰好相反。不占确定空间，不确定的中间值，一般不好引用。
C++11之后右值可以引用, 解决把临时变量占有的外部资源直接给新生成的对象的问题。右值引用避免了程序的开销，增加了程序运行的效率。[说法](https://blog.csdn.net/qq_42418668/article/details/92783329) 引用“&&”

–	字节数量
64位系统指针占8字节，32位占4字节。
但是值类型占用是不分系统数位的。比如：
整型：int 占4位，long也是4个，short站2个
字符型：char一个字节 wchcar_t 占两个
 bool：占1个
浮点：float4个，double8个


–	空类的占用的内存，结构体的占用的字节数，虚函数和虚表
[参考](https://blog.csdn.net/chenchong08/article/details/7620984?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.baidujs&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.baidujs)
空类占一个字节
一个不含虚函数的成员也是1，类的非虚成员函数是不计算在内的,不管它是否静态。
虚函数：一般类内部产生指向虚函数的指针,32位的计算机每个指针占4个字节
结构体涉及子节对齐，顺序排列，不足的转下一行，并且与最长的对齐。静态成员C++不占分配的位置

–	多继承与多重继承
多继承是指一个子类继承多个父类。多继承对父类的个数没有限制，继承方式可以是公共继承、保护继承和私有继承。
[三种继承](https://www.cnblogs.com/ktao/p/8579115.html) 
Public继承之后，public成员保持不变，private成员不可见，protected成员也保持不变。
Protect继承之后，public变成了protected，protected保持不变，private成员不可见
Private继承之后，public和protected都变成了private，private成员不可见

–	虚析构函数的作用
当用一个基类的指针删除一个派生类的对象时，派生类的析构函数会被调用。


–	前置++和后置++的本质区别，原理是什么
i++：返回是的const，不能在进行赋值操作了
++i：返回的事地址，还可以进行赋值操作
前置++的效率更高，理由是：后置++会生成临时对象。

–	map，set的原理，别的容器会那些
[参考](https://blog.csdn.net/qq_33904512/article/details/103706016)
vector：动态改变存储空间，array是指定大小，如果想要扩大需要把内部的值复制到大内存里。
map：Map是关联容器，以键值对的形式进行存储，方便进行查找，关键词起到索引的作用，值则表示与索引相关联的数据，以红黑树的结构实现，插入删除等操作都可以在O(log n)时间内完成
array：Set是关联容器，set中每个元素都只包含一个关键字，set支持高效的关键字查询操作---检查每一个给定的关键字是否在set中，set是以红黑树的平衡二叉检索树结构实现的，支持高效插入删除，插如元素的时候会自动调整二叉树的结构，使得每个子树根节点键值大于左子树所有节点的键值，小于右子树所有节点的键值，另外还得保证左子树和右子树的高度相等


–	C++内存空间划分，值类型和引用类型
值类型：int double bool char decimal struct enum
引用类型：string 自定义类
值类型的值存储在内存的栈当中
引用类型的值存储在内存的堆中

C#的垃圾回收原理


–	new和delete本质是什么，和malloc和free的区别
[参考](https://www.cnblogs.com/maluning/p/7944231.html)
new/delete 动态分配/回收的对象存储空间
使用new操作符申请内存分配时无须指定内存块的大小，编译器会根据类型信息自行计算。而malloc则需要显式地指出所需内存的尺寸。


内存泄漏如何造成的，如何避免
可以使用智能指针


–	智能指针有哪些。[参考](https://www.cnblogs.com/wxquare/p/4759020.html)
C++11中引入了智能指针的概念，方便管理堆内存。使用普通指针，容易造成堆内存泄露（忘记释放），二次释放，程序发生异常时内存泄露等问题等，使用智能指针能更好的管理堆内存
智能指针包含在头文件<memory>中，shared_ptr（多个）、unique_ptr（唯一一个，不可拷贝）、weak_ptr(配合share_ptr使用)


–	动态链接库和静态链接库的区别，exe是静态链接还是动态链接
exe是静态，dll是动态
动态链接库是软件需要用到库中的函数时才调用DLL；静态库是在程序编译时直接编译程序

–	指针和引用的区别
可以把引用理解成变量的别名。定义一个引用的时候，程序把该引用和它的初始值绑定在一起，而不是拷贝它。

–	宏定义，常见的宏指令，define，ifdef那些
COMDEF_H防止重定义，_DEBUG

–	null,nullptr的区别
Null是0，是宏定义
C++ 11之后为了解决二义性，出了nullptr

### 逻辑运算与位运算
!是逻辑运算符(与||，&&是一类符号)，表示逻辑取反，可以把非0值变成0，把0值变为1
–	~是位运算符（与|，&，^(异或)是一类符号），表示按位取反，在数值的二进制表示上，将0变为1，将1变为0

### VS IDE配置
[菜单栏配置](https://jingyan.baidu.com/article/3c343ff7a90d440d37796396.html)
2.OpenCV的[路径配置](https://blog.csdn.net/qq_45771209/article/details/106772812)
3..lib/.h/dll的引用[方法](https://blog.csdn.net/li975242487/article/details/88223669)


MFC与Opencv合用基础
字符转换
–	cv::String和CString互转[方案](https://blog.csdn.net/u011555996/article/details/97046315)
开始一个MFC
–	[创建](https://nprogram.hatenablog.com/entry/2017/06/12/122402)
    
    
### 符号
：放在函数后面用于初始化    
 
