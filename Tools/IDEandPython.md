### Pycharm

- 设置自动换行：setting + wraps
- 全局查找 按两下shift

### Python

@ classmethod 相当于类中的静态函数
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

@property 装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。


### Parser的写法

```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--param1",type=str,default="param1",help="this is parma1") 
#help仅会包含一些说明字符
parser.add_argument("--param2",type=str,default="param2",help="this is parma2") 
args = parser.parse_args()
print(args.param2) #直接拿这个输入的名字就可以 不要包含字符，有--和没有是一致的
```

args.param2还可以二次赋值


### 矩阵乘法

(np.mat(A))*(np.mat(B))  
或者np.matmul
其中 * ，np.multiply都是对位点乘

简洁写法

初始化一个零表
[0] * n n代表想要初始化的数目
[[0] * 5] * 5 这样可以初始化一个0矩阵


networkX


Python 代码规范

https://www.runoob.com/w3cnote/google-python-styleguide.html


Python 位运算

[位运算](https://blog.csdn.net/lemon4869/article/details/107003387)
[进制转化](https://www.cnblogs.com/gkx0731/p/9501276.html)
int('01001',2) -> 2转10
bin(13) = ‘0b1101’ -> 10转2


在Python C/C++ 混合编程

Python -> .dll -> C
Cython: Cython是结合了Python和C的语法的一种语言,可以简单的认为就是给Python加上了静态类型后的语法。

[what is Cython](https://zhuanlan.zhihu.com/p/49573586)
[Python2dll](https://blog.csdn.net/zmr1994/article/details/90703017)
add when using cython function
%%cython

[C++/C/Python](https://blog.csdn.net/lengyue2015/article/details/82154072)混合编程

Py_Initialize();
XXXXXXXX
内容	
Py_Finalize();


线程锁

Python Multi-Threads
进程间通讯（IPC）: 进程间共享信息
进程：程序的一次执行，每个进程都有自己的地址空间、内存、数据栈以及其他辅助数据。进程之间内存空间、数据栈都是相互独立的
pid:唯一标识符来标识进程，使用kill杀死进程 kill pid
线程：所有的线程运行在一个进程中，共享相同的运行环境。
主线程:创造一个进程的时候，会创造一个线程，这个线程被称为主线程,一个进程里只有一个主线程。

Python全局锁机制（GIL）:

thread create: a = threading.Thread(target=func)
thread start: a.start()
thread end:a.join()
防止并行冲突:需要独占资源，比如文件的读写
互斥锁： 
加锁操作完后一定要释放，否则会变成死锁
加锁 acquire 释放锁 release 
什么是 “可重入”，可重入就是说某个线程已经获得某个锁，可以再次获取锁而不会出现死锁。
if there is no release threading.Lock() will stack the thread, while threading.RLock() will not mlock.release() 

e.g.
    import threading
    mlock = threading.Lock()      #mlock  = threading.RLock() 可重入锁，用法一样，防止死锁。
    num = 0
    def a():
        global num
        mlock.acquire()                #加锁 
        num += 1                       #你要执行的代码 ，需要独占资源，比如文件的读写。
        mlock.release()              
        print num
    for i in xrange(0,10):
        d = threading.Thread(target=a)
        d.start()
前面介绍的是自己将自己给锁死了，这种情况相对来说较少，更多的情况是这样的：线程 A 得到某个资源 R1，同时去申请资源 R2，线程 B 得到了资源 R2，同时去申请资源 R1。这时就出现了死锁，线程 A 因为得不到资源 R2 而一直处于等待状态，线程 B 也因为得不到资源 R1 而一直处于等待状态。下面的代码演示了这种情况。 

表示无穷大

float(‘inf’)


yield关键字：返回是迭代器的一个值，不需要有个表来存储所有的值

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1
 
for n in fab(5): 
    print n
    
返り値

def 関数名(引数1, 引数2, ...) -> "返り値の型名":
    処理内容
    
numpy

矩阵加法np.add()：直接用加号相当于concate
随机数组 np.random.rand()
初始化一个某值矩阵 np.full((col,row),v,dty pe=np.float)


图形化界面
[tkinter](https://zhuanlan.zhihu.com/p/75872830?from_voters_page=true)

打包
pip3 install pyinstaller / conda install -c conda-forge pyinstaller
pyinstaller darknet_gui.py --onefile


三个点 […],代表前面的所有。
a = np.array([[[1,2,21],[3,4,34]],[[5,6,56],[7,8,78]]])
等效：
a[...,1:2] == a[:,:,1:2]





