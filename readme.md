# Chatsubo-e 茶壺絵

🍵

aka drawnk i guess

## Hardware and rpi system setup

https://brachiograph.readthedocs.io/en/latest/index.html

https://github.com/evildmp/BrachioGraph

`ssh pi@raspberrypi.local`

`source env/bin/activate`

`cd chatsubo-e` 

`sudo pigpiod`  (will return error `Can't initialise pigpio library` if command has been ran since turning on. ok to procede)

## Building the instance (as of now)

```
python3

from brachiograph import BrachioGraph
bg = BrachioGraph(inner_arm=11, outer_arm=15, servo_1_degree_ms=10, servo_2_degree_ms=10, servo_2_centre=1450, pw_down=910, pw_up=860, bounds=[-10.0, 9.0, 2.0, 20.0])

bg.set_angles(angle_1=90, angle_2=90)  
bg.drive_xy()
# move x: a, s
# move y: k, l

bg.pen.calibrate()
# z: decrease pen motor pulse-width 10µS
# x: increase pen motor pulse-width 10µS
# 0: to exit
```

## Test drawing
```
bg.box()

bg.plot_file('images/gradient.json')
```

## test linedraw
```
from linedraw import *

image_to_json("chatsubo", draw_contours=1)
```

## requirements
if having trouble importing cv2 - 

```
pip install opencv-contrib-python==4.1.0.25
```

