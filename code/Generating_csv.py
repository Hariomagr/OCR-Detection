import numpy as np
import pandas as pd
import cv2
import os

#generating labels
labels = []
for i in range(10):
    labels.append(i)
for i in range(65,91):
    labels.append(chr(i))
for i in range(97,123):
    labels.append(chr(i))
#dataframe empty
cols=[]
cols.append('label')
for i in range(28*28):
    cols.append(str(i+1))
pos=0
dataframe = pd.DataFrame(columns=cols)
all_dir = os.path.join(os.getcwd(),'Fnt')
sub_dir = os.listdir(all_dir)
l=[]
for i in sub_dir:
    a=0
    if(pos<100):
        #image directory
        image_dir = os.path.join(all_dir,i)
        image = os.listdir(image_dir)
        for j in image:
            image_file = os.path.join(image_dir,j)
            #print(image_file)
            img = (cv2.imread(image_file))
            #3d to 2d
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #to 1d
            img = img.ravel()
            #conceeatenate label and pixels
            img=np.concatenate([[labels[pos]],img])
            #print(img)
            dataframe.loc[len(dataframe)]=img
            #l.append(img)
            a+=1
    pos+=1
    print(i,a)
#saving csv file
dataframe.to_csv("image_file.csv")
