# Chatsubo-e 茶壺絵

🍵

aka drawnk i guess

## Hardware and rpi system setup

https://brachiograph.readthedocs.io/en/latest/index.html

https://github.com/evildmp/BrachioGraph

`ssh pi@raspberrypi.local`

`source env/bin/activate`

`cd chatsubo-e`

`sudo pigpiod`

## Testing (as of now)

```
python3

from brachiograph import BrachioGraph

bg = BrachioGraph(inner_arm=11, outer_arm=15, servo_1_degree_ms=10, servo_2_degree_ms=10, pw_down=1120, pw_up=1070, bounds=[3.0, 18.0, 6.0, 21.0])

bg.set_angles(angle_1=90, angle_2=90)  
bg.drive_xy()

# virtual mode 

bg = BrachioGraph(inner_arm=11, outer_arm=15, virtual_mode = True, servo_1_degree_ms=10, servo_2_degree_ms=10, pw_down=1120, pw_up=1070, bounds=[3.0, 18.0, 6.0, 21.0])
```

### test linedraw
```
from linedraw import *

image_to_json("gradient", draw_contours=2, draw_hatch=16)

image_to_json("chatsubo", draw_contours=1)
```

#Calibrate pen lift
```
bg.pen.calibrate()
#z: decrease pen motor pulse-width 10µS
#x: increase pen motor pulse-width 10µS
```

