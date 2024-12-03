from PIL import Image

def main():
    with Image.open('pilar.png') as img:
        print(img.format)
        print(img.size)

main()