### Pycharm

- 设置自动换行：setting + wraps
- 全局查找 按两下shift

### Python

@ classmethod 相当于类中的静态函数
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

@property 装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。


### Parser的写法

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--param1",type=str,default="param1",help="this is parma1") 
#help仅会包含一些说明字符
parser.add_argument("--param2",type=str,default="param2",help="this is parma2") 
args = parser.parse_args()
print(args.param2) #直接拿这个输入的名字就可以 不要包含字符，有--和没有是一致的

args.param2还可以二次赋值


