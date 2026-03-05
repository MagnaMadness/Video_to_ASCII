from PIL import Image
import numpy as np
import cv2
import time
import keyboard
from ffpyplayer.player import MediaPlayer


A_list = ["W", "@", "#", "&", "S", "%", "0" , "?","/", "*", "+", ";", ":", ",", ".", " "]
##pixel//16

# A_list = [
#     '$', '@', 'B', '%', '8', '&', 'W', '#', '*', 'o',
#     'a', 'h', 'k', 'd', 'p', 'w', 'm', 'Z', 'O', '0',
#     'Q', 'L', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'n',
#     'x', 'r', 'f', 't', '/', '|', '(', '1', '{',
#     ']', '_', '~', '<', 'i', ';', ':','"','^', ',',"'", '.', ' '
# ]
##pixel//5

B_list = A_list[::-1]
def main(image, new_width=100, mode = 1):


  width, height = image.size
  ratio = height/width/2
  new_height = int(new_width*ratio)
  image2 = image.resize((new_width, new_height))
  # image2 = image2.convert("L")
  pixels = image2.getdata()
  # s= ""
  if mode==1:
      U_list = A_list
  elif mode==2:
      U_list = B_list

  # for pixel in pixels:
  #     # print(pixel, end=" ")
  #     s+=B_list[pixel//16]
  # image_data = s
  image_data = "".join([U_list[pixel//16] for pixel in pixels])
  num = len(image_data)
  # final = ""
  # for i in range(0, num, new_width):
  #   final+=image_data[i:(i+new_width)]+"\n"
  final = "\n".join(image_data[i:(i+new_width)] for i in range(0, num, new_width))
  print(f"\033[{new_height}A",end="")
  print(final)
path = "Bad Apple.avi"
player = MediaPlayer(path)
time.sleep(0.5)
vidcap = cv2.VideoCapture(path)

# vidcap = cv2.VideoCapture(0)  #to take ur webcam feed as the video
fps = vidcap.get(cv2.CAP_PROP_FPS)
# print(fps)

success, imagecv = vidcap.read()
# frame = 1
print(success)
while success:
    # if frame%factor==0:
    if keyboard.is_pressed('p'):
        print('Keyboard Interrupt')
        break 
    tmp = time.time()
    imagecv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    image_pil = Image.fromarray(imagecv)
    main(image = image_pil, mode = 2, new_width = 600)
    # cv2.imshow('frame',imagecv)
    success, imagecv = vidcap.read()
    # frame+=1
    slp = 1/(fps)+0.00034 - (time.time()-tmp)*1.075
    if slp<0:
        slp = 0
    time.sleep(slp)
vidcap.release()



