# 方便面识别 | Instant Noodles Detection

* [写在前面](#写在前面)
* [背景介绍](#背景介绍)
* [项目结构](#项目结构)
* [实验结果](#实验结果)
* [开发环境](#开发环境)
* [关于作者](#关于作者)

------

## 写在前面

方便面识别是树莓计算机视觉的传统大作业，作为第一次从头开始进行深度学习(目标检测)相关实验，可以在整个作业的过程中很好的学到并使用使用现有深度学习框架。

但是自己也明白，作业只是在使用成熟的框架，对深度学习本身并没有任何实质性的理解，允悲。

在各位学长前辈和同学的共同努力下，我们有了属于同济软件树莓的一套**<u>方便面数据集</u>**，软件学院大团结，树莓大团结

> **【方便面数据集地址(train & valid)】**
>
> - **坚果云**：https://www.jianguoyun.com/p/DTx85AIQnbLZCBidsrID (访问密码：oWCwUh)
> - **百度云**：链接:https://pan.baidu.com/s/1GvUIxbKG8nf_r1g6MjtGuw  密码:5b5i
>
> **【训练后的权重】**
>
> （文件较大，需要科学上网获取）
>
> - **yolov3**：https://drive.google.com/file/d/15noSWF8llqn8tb_9-u8Wu-unTAQYZfxW/view?usp=sharing
> - **yolov4**：https://drive.google.com/file/d/11Hv_DckfhrOPfz1LP2ybo_Xh_SePWQsv/view?usp=sharing
>
> 由于第一次做数据集拍摄、标注和目标检测相关神经网络，效果比较一般，见谅。

在这次作业之后又从0体验了整个目标检测的深度学习实验，如果想自己体验完整的流程可以参考我在浙大暑期实习的这个repo：https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp ，尤其在数据集扩充的时候找到了比较好的实践，可以参考我写的这个repo：https://github.com/doubleZ0108/Data-Augmentation

现在深度学习的门槛越来越低，成熟框架也越来越完善，越来越变成专业调包侠，很多时候环境配置的时间占据了大头；希望之后有机会能弥补这些遗憾，能深入的学习这其中的原理。

这次作业主要参考的最佳实践来自：https://www.youtube.com/watch?v=10joRJt39Ns ，真的是很详细的视频教程，可以0成本完成自定义识别种类的目标检测算法。

<br/>

## 背景介绍

In intelligent retail, one task is to investigate the proportion of each commodity occupying shelves. In this assignment, suppose that you are provided a surveillance video of a shelf and you need to recognize and locate two specific kinds of products, “康师傅香辣牛肉面” and “康师父卤香牛肉面” in real time. You are recommended to use YoloV2 (an object detection approach) for this task.

<img src="https://upload-images.jianshu.io/upload_images/12014150-14535aa28a065f28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200808124537594" width="50%;" />

<br/>

## 项目结构

- `data/`
  - `obj.data`：数据集配置文件(classes | train | valid | names | backup)
  - `obj.names`：待分类数据名称列表
  - `train/`：训练集数据
  - `valid/`：验证集数据
- `src/`
  - `image.c`：替换原始yolo仓库中的对应文件，在bounding box上显示置信度
  - `util/`：工具类脚本
- `yolov3/`
  - `yolov3.ipynb`：基于yolov3的方便面检测实验
  - `yolov3_custom.cfg`：yolov3自定义配置文件
- `yolov4/`
  - `yolov4.ipynb`：基于yolov4的方便面检测实验
  - `yolov4_custom.cfg`：yolov4自定义配置文件
- `video/`
  - `supermarket.mp4`：原始视频
  - `yolov3_result.mp4`
  - `yolov4_result.mp4`
- `doc/document.md`：实验文档

> **【cfg配置参考】**
>
> - `subdivisions=16`：如果报内存不足，将subdivisions设置为32或64
> - `max_batches`：classes*2000，例如有2个类别人和车 ，那么就设置为4000
> - `steps`：80% 到 90% 的max_batches值  比如max_batches=4000，则steps=3200,3600
> - `classes`：全局搜索 [yolo] 可以搜到3次，每次搜到的内容中修改classes=你自己的类别 比如classes=2
> - `filters`：一样先搜索 [yolo] ,每次搜的yolo上一个[convolution] 中 filters=(classes + 5)x3  比如filters=21

<br/>

## 实验结果

- **yolov3识别结果视频**：链接:https://pan.baidu.com/s/1Gyds0z87Ii9vD_xx473eNQ  密码:06qc
- **yolov4识别结果视频**：链接:https://pan.baidu.com/s/1fbif1gN6Ygsk42sNcwz28g  密码:to50

<img src="https://upload-images.jianshu.io/upload_images/12014150-3faf74feb7aa0bfb.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="predictions - 2020-06-20T200151.106" width="50%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-e92738785848c7f2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="predictions - 2020-06-20T201918.731" width="60%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-9dadec73b2839c1c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="predictions (45)" width="60%;" />

<br/>

## 开发环境

- **操作系统**: Linux
- **实验平台**: Google Colab
- **开发语言**: python3 (jupyter notebook)

<br/>

## 关于作者

|   Name   |                        张喆                         |
| :------: | :-------------------------------------------------: |
|   学号   |                       1754060                       |
| 指导老师 |                      [张林教授](https://sse.tongji.edu.cn/linzhang/)                       |
| 课程名称 |                     计算机视觉                      |
| 项目名称 |                      目标检测                       |
| 联系方式 | [dbzdbz@tongji.edu.cn](mailto:dbzdbz@tongji.edu.cn) |
