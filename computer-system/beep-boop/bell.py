import time
import sys
import tty
import termios

tty_attrs = termios.tcgetattr(0)
tty.setcbreak(0)

while True:
    try:
        x = sys.stdin.read(1)
        print(f"{ord(x)} - {int(x)}")
        if ord('0') <= ord(x) <= ord('9'):
            for i in range(int(x)):
                sys.stdout.buffer.write(b'\x07')
                sys.stdout.buffer.flush()
                time.sleep(0.5)
    except KeyboardInterrupt:
        termios.tcsetattr(0, termios.TCSADRAIN, tty_attrs)
        break
    finally:
        sys.stdout.buffer.flush()