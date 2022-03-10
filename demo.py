#import dependence
import cv2
import jetson.utils
import tensorrt as trt

input = jetson.utils.videoSource("csi://0")
output = jetson.utils.videoOutput("display://0")

while output.IsStreaming():
    img = input.Capture()
    output.Render(img)
    