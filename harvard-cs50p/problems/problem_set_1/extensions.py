#https://cs50.harvard.edu/python/2022/psets/1/extensions/

def main():
    file_name = input("File name: ").lower().strip()
    print(media_type(file_name))

def media_type(file_name):
    extensions = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]
    for extension in extensions:
        if extension in file_name:
            if file_name.endswith(".txt"):
                return "text/plain"
            elif file_name.endswith(".zip") or file_name.endswith(".pdf"):
                return "application/zip" if file_name.endswith(".zip") else "application/pdf"
            else:
                return f"image/{extension.replace(".","")}" if not file_name.endswith(".jpg") else "image/jpeg"
    else:
        return "Enter a valid extension"
        
main()