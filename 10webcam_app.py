import cv2

imgcap=cv2.VideoCapture(0)
result=True

while(result):
    ret,frame=imgcap.read()
    cv2.imwrite("image1.jpg",frame)
    result=False
    print("snapshot taken")
imgcap.release()