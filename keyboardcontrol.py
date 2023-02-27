from djitellopy import tello
import keypress as kp
from time import sleep
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())



def getKeyboardInput():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("a"): lr = -speed
    elif kp.getKey("d"): lr = speed
    elif kp.getKey("w"): fb = speed
    elif kp.getKey("s"): fb = -speed
    elif kp.getKey("UP"): up = speed
    elif kp.getKey("DOWN"): up = -speed
    elif kp.getKey("LEFT"): yv = -speed
    elif kp.getKey("RIGHT"): yv = speed
    elif kp.getKey("q"): me.land()
    elif kp.getKey("e"): me.takeoff()
    
    return [lr, fb, up, yv]

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2] ,vals[3])
    sleep(0.05)
    
    
    
    
    
    
    
    
    
    