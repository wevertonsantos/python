from PIL import Image

def main():
    with Image.open('pilar.png') as img:
        #print(img.format)
        #print(img.size)
        img = img.rotate(100)
        img.save('out.png')

main()