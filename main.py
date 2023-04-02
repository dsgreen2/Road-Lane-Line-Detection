import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def region_of_interest(img,vertices):                      #detectes the region of interest from the canny image
    mask=np.zeros_like(img)                               #creating a black image of the same size
    match_mask_color=255                                #setting mask colour to white
    cv.fillPoly(mask,vertices,match_mask_color)           # filling black image with white colour of given vertices
    masked_image=cv.bitwise_and(img,mask)                # applying bitwise and to find the region of interest
    return masked_image

def draw_the_lines(img,lines):                      #addding lines to image
    img=np.copy(img)                                                   #copying the image to another variable
    blank_img=np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)    
    for line in lines:                                              
        for x1,y1,x2,y2 in line:
            cv.line(blank_img,(x1,y1),(x2,y2),(0,255,0),thickness=3)       #creating lines to a plane black image
    img=cv.addWeighted(img,0.8,blank_img,1,0.0)                         #merging image with lines with original image
    return img

def process(image):                      #method to detect road lane line in the image
    height=image.shape[0]
    width=image.shape[1]
    region_of_interest_vertices=[                      #finding the vertices of region_of_interest
     
     (0,height),
     (width/2,height/2),     
     (width,height)  
    ]
    real=np.copy(image)

    gray_image=cv.cvtColor(image,cv.COLOR_RGB2GRAY)     #converts from one colorscale to other
    canny_image=cv.Canny(gray_image,100,120)             #edge detectionn
    
    cropped_image=region_of_interest(canny_image,
                    np.array([region_of_interest_vertices],np.int32),)
    
     
    lines=cv.HoughLinesP(cropped_image,          #detecting lines from region of interest
                   rho=2,
                   theta=np.pi/60,
                   threshold=50,
                   lines=np.array([]),
                   minLineLength=40,
                   maxLineGap=100)
    
    image_with_lines=draw_the_lines(real,lines)       #addding lines to image
    return image_with_lines                            
    
cap=cv.VideoCapture("E:\IT Project\WhatsApp Video 2022-07-15 at 9.40.22 AM.mp4")     #reading the video
while(cap.isOpened()):
    ret,frame=cap.read()     #cv2.VideoCapture.read() function returns two value, one is boolean that tells whether the reading happended successfully or not, oteher is a frame of video
    frame=process(frame)
    cv.imshow("Video with lines",frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()
