# RoboticArm

## How to Configure

1. Connect Raspberry pi to the OWI Robotic ARM through USB.
2. Turn on OWI Robotic ARM
3. Run this program

## How to Run

python roboArm.py arg1 arg2

### Required Arguments:

* arg1 = command
  * rc = Rotate Base Clockwise
  * rcc = Rotate Base Counterclockise
  * s+ = Shoulder Up
  * s- = Shoulder Down
  * e+ = Elbow Up
  * e- = Elbow Down
  * w+ = Waist Up
  * w- = Waist Down
  * g+ = Grip Open
  * g- = Grip Close
  * l+ = Light On
  * l- = Light Off
  * help = show usage guide

* arg2 = duration in millisecond

