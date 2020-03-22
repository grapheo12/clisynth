import sys
import tty
import termios
import simpleaudio as sa

from frequency import *

keys = ["a", "w", "s", "e", "d", "f", "t", "g", "y", "h", "u", "j"]
scale = int(sys.argv[1])
key_map = {keys[i]: note_cycle[i] + str(scale) for i in range(len(keys))}
key_map["k"] = note_cycle[0] + str(scale + 1)
key_map[" "] = "G1" #Bass

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
try:
    tty.setraw(sys.stdin.fileno())
    while True:
        ch = sys.stdin.read(1)
        if ch == "`":
            break
        note = key_map.get(ch, 'silence')
        print(note + "|", end="")
        pl = sa.play_buffer(samples[note], 1, 2, sample_rate)
        pl.wait_done()
        del pl
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    
