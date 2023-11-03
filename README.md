# Pothole-detection-using-a-self-driving-car

Using the Tiny YOLOv4 and Raspberry Pi for object detection, especially in pothole detection, is an efficient and useful option for real-time or embedded computer vision tasks YOLOv4 is known for its minimal computing resources, exhibiting high speed and performance. The "Tiny" variant is specifically designed for use on low computational power devices, such as the Raspberry Pi.

The Tiny YOLOv4 prototype shows real-time object recognition capabilities even when installed on a Raspberry Pi device. Low latency is critical in applications such as surveillance, robotics, and the Internet of Things (IoT).While tiny YOLO sacrifices on some accuracy compared to the full YOLOV4 model, it still provides necessary detection accuracy. The YOLOv4 model is characterized by its open-source nature, allowing for unrestricted access to its 

Upon configuring the Raspberry Pi to record live video via the camera module. OpenCV is employed for real-time video frame processing and the development of algorithms aimed at detecting potholes within the images.
camera_video.py contains the code for Pothole detection

OpenCV in C++ on a Raspberry Pi to perform lane detection on images or video streams is a common and useful computer vision application. Lane detection can be a critical component of autonomous vehicles or driver-assistance systems. To capture video, using Raspberry Pi camera module and want to interface it with OpenCV in C++, the RaspiCam\_Cv library is used, which provides a convenient way to capture video from the Raspberry Pi camera using OpenCV. Then we converted the captured frame to RGB, defined a region of interest to focus on the area where the lanes are expected and the changed the perspective of the frame to a bird's eye view perspective. On the changed perspective frame we convert the image first to grayscale, then to a binary image by setting a threshold. Edge detection is performed on the binary image using the Canny() operation. The final set of the image processing involves recognising the edges of the lane and the centre of the lane so the car can align itself as and when necessary.

![car](https://github.com/arzoolakhani/Pothole-detection-using-a-self-driving-car/assets/111573266/de849526-97e9-47bd-9147-fc5260a171cb)
