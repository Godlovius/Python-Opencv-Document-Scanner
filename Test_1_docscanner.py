import numpy as np
import cv2
import imutils
from matplotlib import pyplot as plt
cap=cv2.VideoCapture(0)
ret,img=cap.read()
img1=img.copy()
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('Ee',img1)

img1=cv2.bilateralFilter(img1,7,17,17)
cv2.imshow('Ede',img1)
img1=cv2.Canny(img1,30,200)
cnts=cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#cnts=np.asarray(cnts,dtype='uint8')

cnts=imutils.grab_contours(cnts) 
cv2.imshow('Edge',img1)
print(' var  data type',cnts  )
#print("Hi")


img=cv2.drawContours(img,[cnts],-1,(255,255,0),3)

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
for c in cnts:
    peri=cv2.arcLength(c,True)
    point=cv2.approxPolyDP(c,0.015* peri,True)
    if len(approx)==4:
       doc=approx
       break
for coord in doc:
    cx=coord[0]
    cy=coord[1]
sx=sort(cx,reverse=False)
sy=sort(cy,reverse=False)
gx=sort(cx,reverse=True)
gy=sort(cy,reverse=True)
for c in doc:
    if c[0]==sx and c[1]==sy:
       tl=(c[0],c[1])
    if c[0]==gx and c[1]==sy:
       tr=(c[0],c[1])
    if c[0]==sx and c[1]==gy:
       bl=(c[0],c[1])
    if c[0]==gx and c[1]==gy:
       br=(c[0],c[1])
tltr=np.sqrt(((tr[0]-tl[0])**2)+((tr[1]-tl[1])**2))
blbr=np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
trbr= np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
tlbl= np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
pts1=[tl,tr,bl,br]
pts2=[(0,0),(tltr-1,0),(0,tlbl-1),(blbr-1,trbr-1)]
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(600,600))
#Now crop the doc from the image
scan=img[0:trbr-1,0:tltr]
cv2.imshow('Scan',scan)
#To be be continued


    






      
