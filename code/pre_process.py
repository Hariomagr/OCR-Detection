import os
import ocr
import cv2
import shutil
from PIL import Image
#generting labels#
labels = []
for i in range(10):
    labels.append(i)
for i in range(65,91):
    labels.append(chr(i))
for i in range(97,123):
    labels.append(chr(i)+chr(i))
position=0
#getting all image dir#
all_dir = os.path.join(os.getcwd(),'Fnt')
sub_dir=os.listdir(all_dir)
for i in sub_dir:
    image_dir = os.path.join(all_dir,i)
    image = os.listdir(image_dir)
    for j in image:
        #getting image file
        image_file = os.path.join(image_dir,j)
        #checking if directory exists, if not then make
        if not os.path.exists(os.path.join('pre-processed1',str(labels[position]))):
            os.makedirs(os.path.join('pre-processed1',str(labels[position])))
        #pre-processing using opencv
        pre_img=ocr.pre_process(image_file)
        path=(os.path.join(os.getcwd(),'pre-processed1',str(labels[position])))
        #saving image
        cv2.imwrite(os.path.join(path,j),pre_img)
        print(path)
    position+=1
        
#http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishFnt.tgz#
