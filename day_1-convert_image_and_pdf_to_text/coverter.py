# import neccessary libraries
# import pandas as pd
import os
from PIL import Image
import PyPDF2, pytesseract


# declaration of functions then implemetation below


# function to convert pdf to string
"""
steps:
1. initialize an empty variable
2. open the pdf file
3. initialize a pdf reader object
4. iterate each pages in the pdf file
5. for each pages extract the text and store it in our variable
6. return your string output
"""

def pdf2text(path):
    text = ''
    with open(path, 'rb') as file:
        pdfReader = PyPDF2.PdfReader(file)
        page_length = len(pdfReader.pages)
        for _ in range(page_length):
            page = pdfReader.pages[_]
            text += page.extract_text()

    return text

# function to convert image to text
"""
steps:
1. open the image
2. convert the image to string using pytesseract a library that uses the google 
    ocr functionality
3. return your string output
"""
def Img2text(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text



# function to convert pdf or images to text
"""
steps:
1. get the entire file extension we accept
2. split the filepath to get the file extension
3. convert it to lower case and checl if it matches anyof the file extensions we listed
4. return the converted version else return an error message
"""

def Convert2Text(file):
    image_ext = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    pdf_ext = {'.pdf'}

    file_, path_ext = os.path.splitext(file)

    if path_ext.lower() in image_ext:
        result = Img2text(file)

    elif path_ext.lower() in pdf_ext:
        result = pdf2text(file)

    else:
        result = 'file not compactible'

    return result


# store the path of whatever 
filepath = '/home/ricardoblinks/Documents/updatedCv.pdf'

# call the convert2text function and pass the filepath
converted = Convert2Text(filepath)

#printed result 
print(converted)

