
Windows平台专用——>DirectX 11

通用平台的Opengl

Vulkan[介绍](https://www.zhihu.com/question/424430509)

[参考](https://zhuanlan.zhihu.com/p/161950497)

PBR有两种主要的工作流

- Metallic/Roughness（金属值/粗糙度）
- Specular/Glossiness（镜面反射/光泽度）

渲染管线的作用：

- 是将物体3D坐标转变为屏幕空间2D坐标，二是为屏幕每个像素点进行着色
-	一般流程

分别是：顶点数据的输入、顶点着色器、曲面细分过程、几何着色器、图元组装、裁剪剔除、光栅化、片段着色器以及混合测试

广泛使用：Linear BS，缺点，会出现Skin collapse, Candy wrapper artifacts等现象

使用PBS(Physical based simulation)去做animation等应用
