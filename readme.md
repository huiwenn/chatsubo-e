# Chatsubo-e 茶壺絵

🍵

## Hardware and rpi system setup
https://brachiograph.readthedocs.io/en/latest/index.html
https://github.com/evildmp/BrachioGraph
source env/bin/activate


## Testing (as of now)

```
sudo pigpiod
python3

from brachiograph import BrachioGraph
bg = BrachioGraph(inner_arm=10, outer_arm=19, servo_1_degree_ms=10, servo_2_degree_ms=-10)

bg = BrachioGraph(inner_arm=10, outer_arm=19, servo_2_degree_ms=-10, bounds=[-15, 5, -2, 12])


bg.set_angles(angle_1=-90, angle_2=90)  # should move the inner arm 5 degrees anti-clockwise
bg.drive_xy()


```