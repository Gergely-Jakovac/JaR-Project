import sys
import mimetypes
import os.path

# modifying path at runtime to be see our imports:
sys.path.insert(1, '/home/jakovac/Desktop/Családi Cég/Adaptive-Version-Tracking-System/')

from AVTS import *
from raw_environment import *

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


# HTML templates are .html files, that are interpreted with the AVTS templating language
def openHTMLTemplate(template_path):
    elems = []
    stream = lambda line: elems.append(line)
    endl = lambda: elems.append("\n")
    begl = lambda: None
    environment = RawEnvironment(stream, begl, endl)
    f = open(template_path)
    avts = AVTS(environment, f)
    avts.handle()
    f.close()
    data = "".join(elems)
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

#!!! duplicate code:
def generateErrorHTML(error_code, template_path):
    elems = []
    stream = lambda line: elems.append(line)
    endl = lambda: elems.append("\n")
    begl = lambda: None
    environment = RawEnvironment(stream, begl, endl)
    f = open(template_path)
    avts = AVTS(environment, f)
    avts.setVariable('error_code', error_code)
    avts.handle()
    f.close()
    data = "".join(elems)
    return bytes(data, encoding="utf-8")

