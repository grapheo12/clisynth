import sys
import numpy as np
from scipy.io.wavfile import write

from frequency import *

with open(sys.argv[1], "r") as f:
    txt = f.read()
    notes = txt.split("|")[:-1]

    stk = []
    for note in notes:
        stk.append(samples[note])
    print(len(stk))
    song = np.hstack(tuple(stk))
    print(song.shape)
    write(sys.argv[2], sample_rate, song)
