#https://cs50.harvard.edu/python/2022/psets/1/extensions/

def main():
    file_name = input("File name: ").lower().strip()
    print(media_type(file_name))

def media_type(file_name):
    extensions = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]
    for extension in extensions:
        if file_name.endswith(extension):
            if extension == ".txt":
                return "text/plain"
            elif extension == ".pdf" or extension == ".zip":
                return f"application/{extension.replace(".","")}"
            else:
                return f"image/{extension.replace(".","")}"
        else:
            return "Enter a valid extension"
        
main()