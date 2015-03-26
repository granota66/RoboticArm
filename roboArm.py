# ROBOT ARM CONTROL PROGRAM
# import the USB and Time libraries into Python
import usb.core, usb.util, time
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
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,
            1000)
    # Stop movement after waiting specified time
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,
            1000)

def switch(duration, command):
    return{
        'rc': MoveArm(duration,[0,1,0]),
        'rcc': MoveArm(duration,[0,2,0]),
		's+': MoveArm(duration,[64,0,0]),
		's-': MoveArm(duration,[128,0,0]),
		'e+': MoveArm(duration,[16,0,0]),
		'e-': MoveArm(duration,[32,0,0]),
		'w+': MoveArm(duration,[4,0,0]),
		'w-': MoveArm(duration,[8,0,0]),
		'g+': MoveArm(duration,[2,0,0]),
		'g-': MoveArm(duration,[1,0,0]),
		'l+': MoveArm(duration,[0,0,1]),
		'l-': MoveArm(duration,[0,0,1]),
		'exit': break
        }.get(command, print 'Please enter a correct movement')


while True:
   	command = raw_input("Enter the movement:")
	duration = raw_input("Enter the duration:")
	switch(duration,command)



#MoveArm(1,[0,1,0]) # Rotate Base Anti-clockwise
#MoveArm(1,[0,2,0]) # Rotate Base Clockwise
#MoveArm(1,[64,0,0]) # Shoulder Up
#MoveArm(1,[128,0,0]) # Shoulder Down
#MoveArm(1,[16,0,0]) # Elbow Up
#MoveArm(1,[32,0,0]) # Elbow Down
#MoveArm(1,[4,0,0]) # Wrist Up
#MoveArm(1,[8,0,0]) # Wrist Down
#MoveArm(1,[2,0,0]) # Grip Open
#MoveArm(1,[1,0,0]) # Grip Close
#MoveArm(1,[0,0,1]) # Light On
#MoveArm(1,[0,0,0]) # Light Off
