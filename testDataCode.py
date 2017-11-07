import numpy as np
import cv2
import os

for filename in os.listdir('testDataSet'):
    img = cv2.imread(os.path.join('testDataSet',filename))
    length =  len(filename)
    face_cascade = cv2.CascadeClassifier('haarFiles/haarcascade_frontalface_alt.xml')
    a=[]
    i = 0

    num_rows, num_cols = img.shape[:2]

    while(i<360):
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), i, 1)
        img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
        gray = cv2.cvtColor(img_rotation, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        if(len(faces)>0):
            a.append(1)
        else:
            a.append(0)
        cv2.waitKey(10)
        i+=5

    #Current values
    current_count = 0
    current_start = 0

    #Maximum values
    max_count = 0
    max_start = 0
    max_end = 0

    #Initial segment if starts with initial element
    initial_index = 0
    initial_end = 0

    #Number of entries in the array .... 360/5 = 72
    list_length = len(a)

    for i in range(list_length):
        if(a[i]==1):
            if(i==0):
                initial_index = 1
            if(initial_index==1):
                initial_end += 1
            if(current_count==0):
                current_start = i
            current_count += 1
        elif(current_count>max_count):
            max_count = i-current_start
            max_start = current_start
            max_end = i-1
            current_count = 0
        if(a[i]==0):
            initial_index = 0
            current_count = 0

    if(a[list_length-1]==1):
        if(list_length - current_start > max_count):
            max_count = list_length - current_start
            max_start = current_start
            max_end = list_length - 1

    median = -1

    if((a[0]==1 and a[list_length-1]==1) and initial_end!=list_length):
        if(initial_end+list_length-current_start > max_count):
            median = (current_start+(initial_end+list_length-current_start)/2)%list_length
    else:
        median = max_start + (max_end-max_start)/2

    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 5*median, 1)
    img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
    gray = cv2.cvtColor(img_rotation, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        cv2.imwrite("results/"+filename,img_rotation[y:y+h,x:x+w])
    print("Done")
print("Completed")
