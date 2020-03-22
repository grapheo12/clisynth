"""
0.25s samples of all notes from A0 to A8
and silence.
"""
import numpy as np

__all__ = ["sample_rate", "interval", "frequencies", "samples", "note_cycle"]

sample_rate = 44100
interval = 0.25
space = np.linspace(0, interval, int(interval * sample_rate))

note_cycle = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
frequencies = dict()
frequencies["A4"] = 440

i = 9
j = 4
while j <= 8:
    if i % 12 == 0:
        j += 1

    frequencies[note_cycle[i % 12] + str(j)] = frequencies["A4"] * 2 ** ((i - 9) / 12)    
    i += 1

i = 9
j = 4
while j >= 0:
    frequencies[note_cycle[i % 12] + str(j)] = frequencies["A4"] * 2 ** ((i - 9) / 12)
    if i % 12 == 0:
        j -= 1
    i -= 1

frequencies['silence'] = 0

samples = dict()

for k, v in frequencies.items():
    samples[k] = np.sin((2 * np.pi * v) * space)
    samples[k] *= 32767 
    samples[k] = samples[k].astype(np.int16)


 

