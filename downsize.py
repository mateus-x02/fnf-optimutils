import pathlib
import math
from PIL import Image
import xml.etree.ElementTree as ET

# run 'python -m pip install Pillow' to install PIL
# usage: python textureDownsize.py 'downsizing factor/divisor' 'path to xml file' 'path to image file'
# Note that both the width and height are downsized (downsize = 2 returns an image 1/4 of the original size)

downsizestr = input('Downsizing Factor: ')
path = input('Path to both (leave no extension): ')
png = path + '.png'
xml = path + '.xml'
downsize = int(downsizestr)

if (downsize % 2 != 0 or downsize == 0):
    raise ValueError("Downsizing factor should be a multiple of 2 for Integer Scaling.")

xmlPath = pathlib.Path() / xml
imgPath = pathlib.Path() / png
tree = ET.parse(xmlPath)
root = tree.getroot()

newImage = Image.open(imgPath)
width, height = newImage.size

ScaleText = open(path + ' Scale.txt',"w+")
ScaleText.write("Hi! You downsized this by x" + downsizestr + " in case you forgot.")

# resample=0 for nearest neighbour, 1 for lanczos, 2 bilinear, 3 cubic, 4 box, 5 hamming
# default uses bilinear cause anything more for sprites is wasted space
newImage = newImage.resize((int(width/downsize), int(height/downsize)), resample=0)
newImage.save(imgPath)
print('Downsized Image')

def scale(value):
    return str(math.floor(int(value)/downsize))
    print('Setted Scale Downsize')
def scalebutTimes(value):
    return str(math.floor(int(value)/downsize))
    print('Setted Scale Upsize (for frameX and frameY')

for subtext in root.findall('SubTexture'):
    subtext.set('x', scale(subtext.get('x')))
    subtext.set('y', scale(subtext.get('y')))
    subtext.set('width', scale(subtext.get('width')))
    subtext.set('height', scale(subtext.get('height')))
    print('Defined Sizes to Scale')

    if (subtext.get('frameWidth') is not None):
        subtext.set('frameWidth', scale(subtext.get('frameWidth')))
        print('Downscaled frameWidth')

    if (subtext.get('frameHeight') is not None):
        subtext.set('frameHeight', scale(subtext.get('frameHeight')))
        print('Downsized frameHeight')
    
    if (subtext.get('frameX') is not None):
        subtext.set('frameX', scale(subtext.get('frameX')))

    if (subtext.get('frameY') is not None):
        subtext.set('frameY', scalebutTimes(subtext.get('frameY')))

tree.write(xmlPath, encoding='utf-8', xml_declaration=True) 

print('DONE! Enjoy your optimized Sprite Sheet!')
