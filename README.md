# MotionMotionGO

记录游戏引擎，动画，动作重定向，风格迁移，内容生成等相关研究，资源和方法。持续更新和补充。

### 游戏引擎学习相关

[Games101](https://www.bilibili.com/video/BV1X7411F744?from=search&seid=16421186143123811718)

### 相关工具的使用

* blender python api
  - 下载blender 然后安装 ```pip install bpy``` 
  - 文档[API](https://docs.blender.org/api/current/index.html)
* Open3D 
  - 下载[release](https://github.com/intel-isl/Open3D/releases)版本，注意不要用PyPi直接install，版本太低了会无法导入obj文件。
  - 文档[API](http://www.open3d.org/docs/release/)

* Maya API
  - 暂时未配置

* All kinds of Converter

### 论文整理
* RigNet [repo](https://github.com/zhan-xu/RigNet)
* Deep Motion Editing [repo](https://github.com/DeepMotionEditing/deep-motion-editing)
* Neural Blend Shapes [repo](https://github.com/PeizhuoLi/neural-blend-shapes)
* MeshCNN [repo](https://github.com/ranahanocka/MeshCNN)
* Deep Mimic[repo](https://github.com/xbpeng/DeepMimic)
* P2P-Net [repo](https://github.com/kangxue/P2P-NET)
* Neural Skinning [demo](https://github.com/FuxiCV/NeuroSkinning)


### 笔记和总结

### 资源获取


A) 动作数据来源
- 卡内基梅隆大学Mocap数据集
Graphics Lab Motion Capture Database 
有tvd，c3d，amc，mpg，Animated多种数据格式，只有标准肢体，没有表情和手的动作。每组时长大约为120帧
[网址](http://mocap.cs.cmu.edu/)
转换好的bvh下载地址
[网址](https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion)

- MIXAMO
包含2500左右单人模型和动画，有手指动画，没有表情，fbx格式
[网址](https://www.mixamo.com/#/)
基于MIXAMO的预处理模型（BFA）：已经进行了按照模型进行了预处理，bvh文件
[网址](https://github.com/DeepMotionEditing/deep-motion-editing)
[网址](https://github.com/ChrisWu1997/2D-Motion-Retargeting/blob/master/dataset/Guide%20For%20Downloading%20Mixamo%20Data.md)

- Iclone
付费动画资源，包含上千种日常场景下的人体动画，支持定制人物模型，动作捕捉等。
[网址](https://www.reallusion.com/JP/iclone/default.html)

MikuMiku Dance
用户自制二次元舞蹈动画资源，包含自制，动捕等多种动作资源。目前没有找到有标记好的完整数据集，需要爬取。
[网址](https://sites.google.com/site/mikumikubeat/motion-data)

ROKOKO
包含表情，手部，身体等动作的Mocap数据提供网站。包含多种不同场景下的资源。但是大部分资源需要付费。

UBI motion matching Dataset
[repo](https://github.com/ubisoft/Ubisoft-LaForge-Animation-Dataset)

B) 人物模型
- 支持定制人物的网站上的已有资源和自制资源
IClone，Metahuman
- 3D模型资源站
CGTrader，SketchFab
[site](https://sketchfab.com/tags/human)

SMPL [site](https://smpl.is.tue.mpg.de/)


### 杂项

- 常用文件格式说明
  - [obj](https://github.com/RavenLeeANU/MotionMotionGO/blob/main/Notes/OBJ-file-description.md)
  - fbx
  - bvh

- 业界
  - [UBI motion matching](https://montreal.ubisoft.com/en/introducing-learned-motion-matching/)

