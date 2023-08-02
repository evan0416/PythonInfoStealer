from PIL import Image
import os


for root,dirs, files in os.walk(".\\"):
    height =0
    print(root)
    
    for file in files:
        if not file.endswith(".png"):
            continue
        path = root + os.sep +file
        img = Image.open(path)
        if img.width != 690:
            continue
        print(path, img.width, img.height)
        height +=img.height
    print(height)
    input()