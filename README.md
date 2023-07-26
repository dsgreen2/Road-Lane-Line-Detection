# Road-Lane-Line-Detection
Takes a video input and identifies the lines marking the edges of road.<br>
Hough transform is used for detecting lane lines.
<br>One of the many steps involved during the training of an autonomous driving car is lane detection, which is the preliminary step.

Lane detection involves the following steps:<br><br>
1.Capturing and decoding video file: We capture the video using VideoCapture object and after the capturing has been initialized every video frame is decoded (i.e. converting into a sequence of images).<br>

2.Grayscale conversion of image: The video frames are in RGB format, RGB is converted to grayscale because processing a single channel image is faster than processing a three-channel colored image.
<br><br>
3.Reduce noise: Noise can create false edges, therefore before going further, it’s imperative to perform image smoothening. Gaussian filter is used to perform this process.
<br><br>
4.Canny Edge Detector: It computes gradient in all directions of our blurred image and traces the edges with large changes in intensity. For more explanation please go through this article: Canny Edge Detector.
<br><br>
5.Region of Interest: This step is to take into account only the region covered by the road lane. A mask is created here, which is of the same dimension as our road image. Furthermore, bitwise AND operation is performed between each pixel of our canny image and this mask. It ultimately masks the canny image and shows the region of interest traced by the polygonal contour of the mask.
<br><br>
6.Hough Line Transform: The Hough Line Transform is a transform used to detect straight lines. The Probabilistic Hough Line Transform is used here, which gives output as the extremes of the detected lines.<br><br>


https://github.com/dsgreen2/Road-Lane-Line-Detection/assets/106010465/7663bf3f-9dba-4af1-97a5-e3490ec50ebe


