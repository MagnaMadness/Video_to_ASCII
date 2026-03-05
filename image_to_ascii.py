from PIL import Image
import numpy as np
import cv2
import time
import keyboard
from ffpyplayer.player import MediaPlayer


A_list = ["W", "@", "#", "&", "S", "%", "0" , "?","/", "*", "+", ";", ":", ",", ".", " "]
#pixel//16

# A_list = [
#     '$', '@', 'B', '%', '8', '&', 'W', '#', '*', 'o',
#     'a', 'h', 'k', 'd', 'p', 'w', 'm', 'Z', 'O', '0',
#     'Q', 'L', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'n',
#     'x', 'r', 'f', 't', '/', '|', '(', '1', '{',
#     ']', '_', '~', '<', 'i', ';', ':','"','^', ',',"'", '.', ' '
# ]
#pixel//5

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
# path = r"C:\Personal Data\Anmol\11B\9I\Songs\TenSura OP 1.mp4"
# path = "Bad Apple.avi"
# # path = r"C:\Personal Data\Anmol\11B\9I\Songs\Raiden Shogun Baal AMV-GMV  [ Sia - Unstoppable] Genshin Impact.mp4"
# player = MediaPlayer(path)
# time.sleep(0.5)
# vidcap = cv2.VideoCapture(path)

# # vidcap = cv2.VideoCapture(0)
# fps = vidcap.get(cv2.CAP_PROP_FPS)
# # print(fps)
# # if fps>30:
# #     factor = 1*round(fps/30)
# # else:
# #     factor = 1
# success, imagecv = vidcap.read()
# # frame = 1
# print(success)
# while success:
#     # if frame%factor==0:
#     if keyboard.is_pressed('p'):
#         print('Keyboard Interrupt')
#         break 
#     tmp = time.time()
#     imagecv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
#     image_pil = Image.fromarray(imagecv)
#     main(image = image_pil, mode = 2, new_width = 600)
#     # cv2.imshow('frame',imagecv)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#     success, imagecv = vidcap.read()
#     # frame+=1
#     slp = 1/(fps)+0.00034 - (time.time()-tmp)*1.075
#     if slp<0:
#         slp = 0
#     time.sleep(slp)
# vidcap.release()
# path = input("Path: ")
# path = r"C:\Users\anmol\Downloads\Indian_Institute_of_Space_Science_and_Technology_Logo.png"
path =r"D:\Anmol-SSD\11B\9I-SSD\rickroll.gif"

imagepil = Image.open(path).convert("L")
main(image = imagepil, mode = 2, new_width = 480)
