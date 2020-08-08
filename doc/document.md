# Instant Noodles Detection Document

* [Solution](#solution)
* [Result](#result)
* [Others](#others)

------

## Solution

I use Yolov3 and Yolov4 for instant noodles detection. And here is the specific process and result of my experiment.

1. Preparation

   1. GPU configuration
   2. some utils

2. Building Darknet

   1. clone darknet from AlexeyAB's famour repository
   2. modify Makefile to enable opencv and GPU for darknet
   3. build darknet

3. Pretrained Yolov3/4 weights

   1. Yolov3 has been trained already on the coco dataset which has 80 classes that it can predict

   2. run detectioins with darknet and Yolov3/4

      ```shell
      !./darknet detect <path to config> <path to weights> <path to image>
      ```

4. Train Our Instant Noodles Object Detector

   1. customer files
      - gather labeled custom dataset(finally I have 358 photos for training)
      - custom `.cfg` file(I change the subdivision, classes, filters and some other hyperparameters)
      - `obj.data` and `obj.names` files
      - `train.txt` file(I wrote a python script for generate train file)
   2. download pre-trained weights for the convolutional layers
   3. train the neural network
   4. test the neural network

（Here is just a brief description of the training process. Please refer to `src/` for details. If you have any questions, please contact me）

<br/>

## Result

some well detected photos

<img src="https://upload-images.jianshu.io/upload_images/12014150-3faf74feb7aa0bfb.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="predictions - 2020-06-20T200151.106" style="zoom:50%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-e92738785848c7f2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="predictions - 2020-06-20T201918.731" style="zoom:50%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-9dadec73b2839c1c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="predictions (45)" style="zoom:50%;" />

<br/>

## Others

training chart for avg loss

<img src="https://upload-images.jianshu.io/upload_images/12014150-17c4a2ef53a9be83.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="chart" style="zoom: 33%;" />

some configuration for yolov3

<img src="https://upload-images.jianshu.io/upload_images/12014150-d9e24d133866532e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="参数" style="zoom: 50%;" />

for yolov3, after about 600 epochs, I have the avg loss less than 2.0

<img src="https://upload-images.jianshu.io/upload_images/12014150-a5a5b162230abfe1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="600" style="zoom:50%;" />

some configuration for yolov4

<img src="https://upload-images.jianshu.io/upload_images/12014150-b81cc588b772a1d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="yolov4初始" style="zoom:50%;" />