from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open('pilar.png') as img:
        #print(img.format)
        #print(img.size)
        img = img.rotate(100)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save('out.png')

main()