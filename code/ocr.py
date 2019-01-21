import cv2
import numpy as np

def pre_process(img):
    #read image
    img = cv2.imread(img)
    #convert to grayscale
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gaussian blur
    img = cv2.GaussianBlur(img,(5,5),0)
    #noise removal
    ret, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    kernel = np.ones((2,2),np.uint8)
    #dilating
    img = cv2.dilate(img,kernel)
    pts = np.empty([0,0])
    pts = cv2.findNonZero(img)
    #min rectangle (contours)
    rect = cv2.minAreaRect(pts)
    drawrect = img.copy()
    #draw rectangle (visulaisation)
    drawrect = cv2.cvtColor(drawrect, cv2.COLOR_GRAY2BGR)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(drawrect,[box],0,(0,0,255),10)
    #cv2.imwrite('rotated_rect.png', drawrect)
    rect = list(rect)
    #checking the tilted angle
    if (rect[1][0] > rect[1][1]):
        temp = list(rect[1])
        temp[0], temp[1] = temp[1], temp[0]
        rect[1] = tuple(temp)
        rect[2] = rect[2] + 90.0
    rect = np.asarray(rect)
    rotated_image = np.empty([0,0])
    M = cv2.getRotationMatrix2D(rect[0], rect[2], 1.0)
    #rotating image
    img=cv2.warpAffine(img, M, (img.shape[1],img.shape[0]))
    img,contours,_ = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    #resizing
    img=cv2.resize(img, (28,28),interpolation = cv2.INTER_AREA)
    #print(img.shape)
    #print(len(img.ravel()))
    #cv2.imwrite('ad.png',img)
    #img[img!=0] = 255
    return img
