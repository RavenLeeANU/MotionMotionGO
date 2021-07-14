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

常见事件
- onclick
- onmouseover
- onload
- onchange


定时执行事件
```
var myVar = setInterval(function(){alert("Hello")},3000);
clearInterval(myVar)
```

### 同步与异步

```
setTimeout(foo,2000) //等待2000ms执行foo
```

### 生命周期
- 创建之后一直存在。
- 当不再引用的时候null，undefined时候成为垃圾对象，被回收。


### Promise
- 可以把异步按照顺序执行
链式调用
[参考](https://blog.csdn.net/u013967628/article/details/86569262)
```
cook()
.then(eat)
    .then(wash)
        .then(function(data){
              console.log(data);
        });   

//做饭
function cook(){
    console.log('开始做饭。');
    var p = new Promise(function(resolve, reject){        //做一些异步操作
        //setTimeout(function(){
            console.log('做饭完毕！');
            resolve('鸡蛋炒饭');
        //}, 1000);
    });
    return p;
}
 
//吃饭
function eat(data){
    console.log('开始吃饭：' + data);
    var p = new Promise(function(resolve, reject){        //做一些异步操作
        setTimeout(function(){
            console.log('吃饭完毕!');
            resolve('一块碗和一双筷子');
        }, 2000);
    });
    return p;
}
 
function wash(data){
    console.log('开始洗碗：' + data);
    var p = new Promise(function(resolve, reject){        //做一些异步操作
        setTimeout(function(){
            console.log('洗碗完毕!');
            resolve('干净的碗筷');
        }, 2000);
    });
    return p;
   }
```

两个等号和三个等号
https://www.cnblogs.com/litsword/archive/2010/07/22/1782933.html
