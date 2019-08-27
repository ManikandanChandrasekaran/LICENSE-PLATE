import cv2
import imutils
import pytesseract
l=0
a=[]
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract'
img=cv2.imread("C:\\Users\\Manikandan\\Desktop\\123.jpg")
img=imutils.resize(img,height=400,width=400)
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g=cv2.bilateralFilter(g,220,100,190)
ret,thresh=cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
t=pytesseract.image_to_string(thresh,lang="eng")
for i in range(len(t)):
    if t[i]=='T':
        l=i
        break
for j in range(l,len(t)):
    if t[j].isupper():
        a.append(t[j])
    elif t[j].isnumeric():
        a.append(t[j])

number="".join(a)
print(number)
