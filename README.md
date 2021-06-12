# HW4
# First Part :
1. Download the files in the "First" dir.
2. Make sure your Xbee is connected, and use  "mbed add http://gitlab.larc-nthu.net/ee2405_2021/bbcar" to get the libarary.
3. Compile the program
4. Exercute "sudo python3 car_control.py /dev/ttyUSB0" to control the car, the 1st input is d1(number), the 2nd one is d2(number), and the 3rd one is the direction(east or west), use "enter" key to seperate 3 inputs.
5. The car would start moving.
# Second Part :
1. Download the files in the "Second" dir, use  "mbed add http://gitlab.larc-nthu.net/ee2405_2021/bbcar" to get the libarary.
2. Connect the OpenMV to your host, and save the "line_d.py" as "main.py" into the OpenMV, then connect it back to the mbed.
3. Compile the program.
4. The car would start moving if there are lines in the lower front of the car.
# Third Part :
1. Download the files in the "Third" dir, use  "mbed add http://gitlab.larc-nthu.net/ee2405_2021/bbcar" to get the libarary.
2. Connect the OpenMV to your host, and save the "AprilTag_d.py" as "main.py" into the OpenMV, then connect it back to the mbed.
3. Compile the program.
4. The car would start moving if there is AprilTag in the front of the car that the camera can see.
