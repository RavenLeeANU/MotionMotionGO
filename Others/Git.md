### 如何在git上精准找项目

[参考](https://blog.csdn.net/bbsyi/article/details/104549967/?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242)

### 配置用法
大小写敏感：
$ git config core.ignorecase false

### pull request

定义
Pull Request 是一种通知机制。你修改了他人的代码，将你的修改通知原来的作者，希望他合并你的修改，这就是 Pull Request。

简书上的[解释](https://www.jianshu.com/p/a31a888ac46b)

pull request 前提是fork了别人的repo，然后在github网站上通过自己fork的repo中的pull request来通知别人。

### 教程
[runoob](https://www.runoob.com/git/git-branch.html)

### 常用命令
https下载私有库
```$ git clone https://{user-name}:{password}@{repo-address}```

### 分支管理
#### 查看分支

```$ git branch```

#### 创建分支
```
$ git branch {branchname}
$ git checkout {branchname}
```
ps: 当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容， 所以多个分支不需要多个目录。

#### 上传分支

–	第一次上传分支的时候需要有个upstream分支，即git branch创建只是在本地，需要在远程也创建

```$ git push --set-upstream origin {branchname}```

–	远程也有的话就直接push

#### 删除分支
```$ git branch -d (branchname)```

#### 合并分支
注意：先checkout到要被merge的分支下，然后再操作merge过来的分支，merge完就把原来的删除就可以了 

```$ git checkout {wait for being merged}```

```$ git merge {new content}```

```$ git branch -d {new content}```


#### 解决冲突
#### 查看冲突
```$ git diff```

冲突在代码中体现：
```<<<<<<< HEAD
this is local modified main branch 

 												
this is remote main branch 
>>>>>>> 9e66037e0f6e32d776846faf4df22abf2d3f4d65
```
手改：剩下一行就行
改完上传
```
$ git add .
$ git commit -m merge
$ git push
```
