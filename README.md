# Instant Noodles Detection

[toc]

------

--2.1创建yolo-obj.cfg 文件，将 yolov4-custom.cfg 中的内容复制到 yolo-obj.cfg里面并做以下修改。

　　--2.1.1修改subdivisions=16(如果报内存不足，将subdivisions设置为32或64)

　　--2.1.2修改max_batches=classes*2000   例如有2个类别人和车 ，那么就设置为4000

　　--2.1.3修改steps为80% 到 90% 的max_batches值  比如max_batches=4000，则steps=3200,3600

　　--2.1.4修改classes,先用ctrl+F搜索 [yolo] 可以搜到3次，每次搜到的内容中 修改classes=你自己的类别 比如classes=2

　　--2.1.5修改filters,一样先搜索 [yolo] ,每次搜的yolo上一个[convolution] 中 filters=(classes + 5)x3  比如filters=21