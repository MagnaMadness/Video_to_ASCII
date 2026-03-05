There are 2 files in this repo for now.
The first one image_to_ascii.py converts any video to ascii animation in grayscale.
The second one, image_to_ascii_colored.py converts any videdo to ascii animation in color (tested in command prompt only).

The audio part doesn't work properly for now so I've commented it, you can try use it if you want (I've marked the lines to uncomment)

To use, 
1. put the path to ur video into the path variable (use the raw formatting if using full path with backslashes, r"").
2. In the line "main(image = image_pil, mode = 2, new_width = 600)" set the new_width to the resolution you want it to be displayed it (you can zoom out in command prompt to see the whole thing).
3. You can press q to stop.

I will add more explaination of the code if need be.


If you want to just convert an image to ascii, you can comment out everything after defining the path variable, and uncomment the last 2 lines.


<img width="1055" height="704" alt="image" src="https://github.com/user-attachments/assets/5e5363d8-7e97-471a-b952-0357a619aabd" />
<img width="991" height="668" alt="image" src="https://github.com/user-attachments/assets/b1164ce1-093f-4045-b30a-7224d869d46c" />

