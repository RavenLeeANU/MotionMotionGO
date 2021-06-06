### 常用快捷键


#### 操作

- Left Click + L 选择所有连通部分
- E         挤出
- G         移动
- R         缩放
- Shift+a   调出添加菜单
- P         选择分离物理
- Ctrl + J  合并物体
- Z键调出视图选项，可以选择线框或者渲染模式。
- Ctrl + D  复制一个物体

#### 菜单

在最左侧的小按钮菜单中，拉到scripting里面。

快捷键 shift+f4

聚焦对应的物体： [/] 键 但是有的时候可能没法正常触发，建议先切一下场景再按。

拖动窗体四个角，可以直接拖出来一个新的窗口。放回去也是相同操作。


#### 插件
- [插件下载](http://www.gfxcamp.com/)
- Faceit 用来Rig人脸，做Blendshape的key，使用简单，付费。
- Rigify 用来Rig和绑定骨骼，免费。
- Better FBX 支持导出/导入fbx，能够大大减少材质丢失，读不进来的问题。

#### 教程
- [Rig Anime风格](https://www.youtube.com/watch?v=G2orwhrl4VU&t=21s) 包含了头发物理模拟方法。

#### 其他
1. 使用Faceit导入UE4中人物骨骼都是零件的问题：需要将模型的object都组合起来，否则导出的就都是零件。并且在合并的时候确保动画都是正常显示的。如果显示不正常则调整合并的顺序使得动画别被合并掉了。
2. blend工程导入的文件不能有中文路径，否则就没法正常导入导出
3. fbx导出的时候使用better fbx能够有效防止材质丢失的问题
4. blender的工程文件换了路径 材质都丢失了？
