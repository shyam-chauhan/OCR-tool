from PIL import Image
from pytesseract import pytesseract


path = "image.png"  #image path
image = Image.open(path)    #oprning image
text = pytesseract.image_to_string(image)   #extracting text
print(text) #printing text
