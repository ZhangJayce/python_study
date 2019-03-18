#安装一个三方库

#介绍一个三方库 Pillow 非常强大的处理图像的工具库

#pip install Pillow

from PIL import Image

im = Image.open(r"C:\Users\ZhangJian\Desktop\DSC_0176.jpg")

print(im.format,im.size)
