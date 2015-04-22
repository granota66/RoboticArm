# ROBOT ARM CONTROL PROGRAM
# Author: Shien Hong

# import the USB and Time libraries into Python
import usb.core, usb.util, time, sys
# Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267,idProduct
        =0x0000)
# Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")
# Create a variable for duration

# Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):
    # Start the movement
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)
    print Duration
    Duration = float(Duration)
    print Duration
    # Stop movement after waiting specified time
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)
    return 1

if len(sys.argv) != 3:
	raise ValueError("This program requires two arguments")
	
command = str(sys.argv[1])
duration = str(sys.argv[2])

if command == 'rc': #Rotate Base Clockwise
	MoveArm(duration,[0,1,0])
elif command == 'rcc': #Rotate Base Clockwise
	MoveArm(duration,[0,2,0])
elif command =='s+': #Should Up
	MoveArm(duration,[64,0,0])
elif command == 's-': #Should Down
	MoveArm(duration,[128,0,0])
elif command == 'e+': #Elbow Up
	MoveArm(duration,[16,0,0])
elif command == 'e-': #Elbow Down
	MoveArm(duration,[32,0,0])
elif command == 'w+': #Waist Up
	MoveArm(duration,[4,0,0])
elif command == 'w-': #Waist Down
	MoveArm(duration,[8,0,0])
elif command == 'g+': #Grip Open
	MoveArm(duration,[2,0,0])
elif command == 'g-': #Grip Close
	MoveArm(duration,[1,0,0])
elif command == 'l+': #Light On
	MoveArm(duration,[0,0,1])
elif command == 'l-': #Light Off
	MoveArm(duration,[0,0,0])
elif command =='help':
	print 'rc: Rotate Clockwise\nrcc: Rotate Counter-Clockwise\ns+: Shoulder up\ns-: Should Down\ne+: Elbow Up\ne-: Elbow Down\nw+: Wrist Up\nw-: Wrist Down\ng+: Grip Open\ng-: Grip Close\nl+: Light On\nl-: Light Off\n'
else:
	print 'Incorrect command. enter "help" for command list.'


