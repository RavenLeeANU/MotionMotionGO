### 概念

image 和 container：image相当是个模板，container是个实例

### 参考文档(Docker 基于Go语言)

- [简单教程：runoob](https://www.runoob.com/docker/docker-image-usage.html)
- 官网：[Docker](https://www.docker.com/get-started)
- 手册：[官方手册](https://docs.docker.com/docker-for-mac/install/)

### Host基础命令行

建立一个容器：
```$ docker run -i -t {ubuntu:15.10} /bin/bash ```

各个参数解析：

-t: 在新容器内指定一个伪终端或终端。

-i: 允许你对容器内的标准输入 (STDIN) 进行交互。

查看所有现存的容器

```$ docker ps -a```

CONTAINER ID: 容器 ID。

IMAGE: 使用的镜像。

COMMAND: 启动容器时运行的命令。

CREATED: 容器的创建时间。

STATUS: 容器状态。

启动该容器
```$ docker start  {CONTAINER ID} ```
```$ docker attach {CONTAINER ID} ```
or

```$ docker exec -it {CONTAINER ID} /bin/bash ```
退出容器

```$ exit```
从host机器上拷贝东西

```$ docker cp {origin.txt} {CONTAINER ID}:/{origin.txt} ```

拷贝文件夹也可以

导出container容器快照
```$ docker export 1e560fca3906 > ubuntu.tar```


### Dockerfile指令
```FROM
FROM centos  //指定的镜像
RUN
RUN yum install wget //运行命令行
RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
RUN tar -xvf redis.tar.gz
```
ps：以上执行会创建 3 层镜像。可简化为以下格式：
```
FROM centos
RUN yum install wget \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && tar -xvf redis.tar.gz
```
