import cv2
import numpy as np
from PIL import ImageGrab

def screenrecoder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1366, 768))
    while (True):
        img=ImageGrab.grab(bbox=(0,0, 1366, 768))
        img_np=np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('Screen Recorder', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()

screenrecoder()