from PIL import Image
import numpy as np
import cv2
import time
import os
# from ffpyplayer.player import MediaPlayer ######################################### UNCOMMENT TO PLAY AUDIO
import keyboard

def rgb_ansi(r, g, b, char):
    return f"\033[38;2;{r};{g};{b}m{char}\033[0m"


A_list = ["W", "@", "#", "&", "S", "%", "0" , "?","/", "*", "+", ";", ":", ",", ".", " "]
#pixel//16

# A_list = [
#     '$', '@', 'B', '%', '8', '&', 'W', '#', '*', 'o',
#     'a', 'h', 'k', 'd', 'p', 'w', 'm', 'Z', 'O', '0',
#     'Q', 'L', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'n',
#     'x', 'r', 'f', 't', '/', '|', '(', '1', '{',
#     ']', '_', '~', '<', 'i', ';', ':','"','^', ',',"'", '.', ' '
# ]
#pixel//5   52

B_list = A_list[::-1]
def main(image, new_width=100, mode = 1):


  width, height = image.size
  ratio = height/width/2
  new_height = int(new_width*ratio)
  image = image.convert("RGB")
  image2 = image.resize((new_width, new_height))
  pixels = list(image2.getdata())
  # s= ""
  if mode==1:
      U_list = A_list
  elif mode==2:
      U_list = B_list

  image_data = []

  for (r, g, b) in pixels:
        brightness = int(0.299*r + 0.587*g + 0.114*b)
        char = U_list[brightness // 16] #16
        # char = "W"
        image_data.append(rgb_ansi(r, g, b, char))
  final = "\n".join(
    "".join(image_data[i:i+new_width])
    for i in range(0, len(image_data), new_width)
    )
  print(f"\033[{new_height}A",end="")
  print(final)
# path = "Bad Apple.avi"
path = r"Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp4"
# player = MediaPlayer(path)  ######################################### UNCOMMENT TO PLAY AUDIO
# time.sleep(0.5)
vidcap = cv2.VideoCapture(path)

# vidcap = cv2.VideoCapture(0)
fps = vidcap.get(cv2.CAP_PROP_FPS)
# print(fps)

success, imagecv = vidcap.read()
print(success)
skadoosh = 0
while success:
    if skadoosh == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
    if keyboard.is_pressed('p'):
        print('Keyboard Interrupt')
        break 
    tmp = time.time()
    imagecv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(imagecv)
    if skadoosh%5==0:           ### This part was added to skip rendering most frames else it would show the video really slowly.
        main(image = image_pil, mode = 2, new_width = 480)

    success, imagecv = vidcap.read()
    # slp = 1/(fps) - (time.time()-tmp)*1.075
    # if slp<0:
    #     slp = 0
    # time.sleep(slp)
    skadoosh+=1
    
vidcap.release()

# imagepil = Image.open(path)
# main(image = imagepil, mode = 2, new_width = 480)

