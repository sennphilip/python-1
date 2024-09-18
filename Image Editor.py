from PIL import Image, ImageEnhance, ImageFilter
import os
path = '/Users/philipsenn/Desktop/TEST/imgs'
pathOut = '/Users/philipsenn/Desktop/TEST/editedImgs'
for i in os.listdir(path):
   img = Image.open(f"{path}/filename")
   edit = img.filter(ImageFilter.SHARPEN). convert('L').rotate(-90)
   factor = 1.5
   enhancer = ImageEnhance.Contrast(factor)
   new_name = os.path.splitext(i)[0]
   edit.save(f'.{pathOut}/{new_name}_edited.jpg')