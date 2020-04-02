import sys
import mimetypes
import os.path

def fileOrDirExists(path):
    if os.path.exists(path): # if it is a file:
        return True

def isBinary(path):
    ext = path.split(".")[-1]
    bins = {"jpg", "jpeg", "png", "bmp", "gif",
            "tiff", "raw", "ico", "pcx",
            "pdf", 
            "otf", "ttf"} #...
    return ext.lower() in bins

def openHTMLTemplate(path):
    with open(path, 'r') as file:
        data = file.read()
    return data

def openRawFile(path):
    with open(path, "rb") as file:
        data = file.read()
    return data
    
def handleFileRequest(path, params):
    try:
        mime = mimetypes.guess_type(path)[0]
        if isBinary(path):
            return (openRawFile(path), mime, 200)
        return (bytes(openHTMLTemplate(path), encoding="utf-8"), mime, 200)
    except (FileNotFoundError, IsADirectoryError): #as e:
        return ( b'', "", 404) # file was not found

def generateErrorHTML(error_code, template_path):
    return bytes(openHTMLTemplate(template_path) , encoding="utf-8")

