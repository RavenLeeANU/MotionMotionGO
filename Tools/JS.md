### 闭包

闭包简单来说就是函数中的函数，也可以把它理解为一种现象，就是说一个函数要访问另外一个目标函数内部的变量，就要在目标函数中再定义一个函数（以此来把作用域链往下延长一段，
目的就是为了利用js在找自由变量时,会沿着作用域链一级一级往上找的特点），并将这个定义的函数return出来，供外部使用。在实际开发中，闭包主要是用来**封装变量，收敛权限**。

[原文链接](https://blog.csdn.net/lidysun/article/details/88367885)

```
var add = (function () {
    var counter = 0;
    return function () {return counter += 1;}
})();
```

### 事件

常见时间
onclick
onmouseover
onload
onchange


定时执行事件
```
var myVar = setInterval(function(){alert("Hello")},3000);
clearInterval(myVar)
```

### 同步与异步

setTimeout(foo,2000) //等待2000ms执行foo
