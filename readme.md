# Chatsubo-e 茶壺絵

🍵

## Hardware and rpi system setup

https://brachiograph.readthedocs.io/en/latest/index.html

https://github.com/evildmp/BrachioGraph

`ssh pi@raspberrypi.local`

`source env/bin/activate`

`sudo pigpiod`

## Testing (as of now)

```
python3

from brachiograph import BrachioGraph

bg = BrachioGraph(inner_arm=10, outer_arm=15, servo_1_degree_ms=10, servo_2_degree_ms=10, pw_down=1100, pw_up=1080, bounds=[3.0, 18.0, 6.0, 21.0])

bg.set_angles(angle_1=90, angle_2=95)  
bg.drive_xy()
```

#Calibrate pen lift
```
bg.pen.calibrate()
#z: decrease pen motor pulse-width 10µS
#x: increase pen motor pulse-width 10µS
```