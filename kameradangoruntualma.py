import cv2
import numpy as np
 
# 0 değeri bilgisayar kamerasını algılar, 1 değeri usb ile takılan kamerayı algılar. 
kamera = cv2.VideoCapture(0)
img = np.zeros((512,512,3),np.uint8)
 
while True:
    ret,goruntu = kamera.read()
 
    cv2.imshow("Kamera", goruntu)
 
 
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
 
kamera.release()
cv2.destroyAllWindows()
