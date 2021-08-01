# Mediapipe-implementation-with-opencv-and-pretrained-face-detection-models
# Face Detection:
MediaPipe Face Detection is an face detection model that comes with 6 landmarks and multi-face support. It is based on BlazeFace, a lightweight and well-performing face detectortailored for mobile GPU inference. 

The detector’s super-realtime performance enables it to be applied to any live viewfinder experience that requires an accurate facial region of interest as an input for other task-specific models, such as 3D facial keypoint or geometry estimation.
















# Detections:
Collection of detected faces, where each face is represented as a detection proto message that contains a bounding box and 6 key points (right eye, left eye, nose tip, mouth

center, right ear tragion, and left ear tragion). The bounding box is composed of xmin and width (both normalized to [0.0, 1.0] by the image width) and ymin and height (both 

normalized to [0.0, 1.0] by the image height). Each key point is composed of x and y, which are normalized to [0.0, 1.0] by the image width and height respectively.

Each facial feature is annotated around a particular landmark.


# Installation and requirements:
 ### python 3.6
 ### mediapipe
 ### opencv == 3.4
 ### 
 





