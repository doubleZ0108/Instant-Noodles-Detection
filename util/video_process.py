import cv2
import os
import numpy as np
from PIL import Image
 
def video2frame(videos_path,frames_save_path,time_interval):
 
  '''
  :param videos_path: 视频的存放路径
  :param frames_save_path: 视频切分成帧之后图片的保存路径
  :param time_interval: 保存间隔
  :return:
  '''
  vidcap = cv2.VideoCapture(videos_path)
  success, image = vidcap.read()
  count = 0
  final_counter = 0
  while success:
    success, image = vidcap.read()
    count += 1
    if count % time_interval == 0:
      final_counter += 1
      cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "/frame%d.jpg" % final_counter)
    # if count == 20:
    #   break
  print(count)

def frame2video(im_dir,video_dir,fps):
  if os.path.exists(im_dir + ".DS_Store"):
    os.remove(im_dir + ".DS_Store")

  im_list = os.listdir(im_dir)
  im_list.sort(key=lambda x: int(x.replace("frame","").split('.')[0]))  #最好再看看图片顺序对不
  # im_list.sort(key=lambda x: int(x[x.find('(')+1:x.find(')')]))

  img = Image.open(os.path.join(im_dir,im_list[0]))
  img_size = img.size #获得图片分辨率，im_dir文件夹下的图片分辨率需要一致

  # fourcc = cv2.cv.CV_FOURCC('M','J','P','G') #opencv版本是2
  fourcc = cv2.VideoWriter_fourcc(*'XVID') #opencv版本是3
  videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
  # count = 1
  for i in im_list:
      im_name = os.path.join(im_dir+i)
      frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
      videoWriter.write(frame)
      # count+=1
      # if (count == 200):
      #     print(im_name)
      #     break
  videoWriter.release()
  print('finish')
 
if __name__ == '__main__':
  # videos_path = 'video/supermarket.mp4'
  # frames_save_path = 'img/'
  # time_interval = 2         #隔一帧保存一次
  # video2frame(videos_path, frames_save_path, time_interval)

  #############################################
  im_dir = 'img/'
  video_dir = 'test.avi'
  fps =  15           #帧率，每秒钟帧数越多，所显示的动作就会越流畅
  frame2video(im_dir, video_dir, fps)