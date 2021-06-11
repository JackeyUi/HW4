import time
import serial
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    d1 = int(input())
    d2 = int(input())
    po = input()
    while(1):
        s.write("/goStraight/run -100 \n".encode())
        time.sleep(0.1 * d2)
        s.write("/stop/run \n".encode())
        time.sleep(0.2)
        if po == 'west':
            s.write("/turn/run -100 -0.3 \n".encode())
            time.sleep(2.2)
        else :
            s.write("/turn/run -100 0.3 \n".encode())
            time.sleep(2.2)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        s.write("/goStraight/run -100 \n".encode())
        time.sleep(0.1 * d1)
        s.write("/stop/run \n".encode())
        break
    return 0

if len(sys.argv) < 1:
    print ("No port input")
s = serial.Serial(sys.argv[1])
while get():
    i = 0