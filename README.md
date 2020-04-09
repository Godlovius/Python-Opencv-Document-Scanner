# Python-Opencv-Document-Scanner
#This is a small project of a program that takes a frame from the laptop's camera then searches for the biggest square/rectangular contour
representing the document or paper and applies a perspective transform to the originally captured frame and then crops the document from the image and shows it.
There are bugs the program can't run I don't understand the issue,the type of the variable "cnts" the return value from cv2.findContours() is neither a scalar nor a numpy array it says the data type=17 when I tried to inquire from python about its type and hence I can't draw the contours with the cv2.drawContours() function therefore I can't procede if anyone can help I will be very grateful 
