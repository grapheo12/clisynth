# CLISynth

So you think you can be the next EDM king!
Here is a damn simple command line synthesizer for you.

WARNING: This is in very early stage.

## Installation

You need Python 3 (tested on 3.7) with `virtualenv`.
Also keep `libaudio2-dev` (or equivalent) installed.

1. Clone the repo:
    
    ```sh
    git clone https://github.com/grapheo12/clisynth.git
    ```

2. Spawn a virtualenv:

    ```sh
    cd clisynth
    virtualenv venv (or python3 -m virtualenv venv)
    source venv/bin/activate
    ```

3. Install dependencies:

    ```sh
    pip3 install -r requirements.txt
    ```

## Usage

In the project directory, run:

```sh
python3 clisynth.py [SCALE] > [OUTPUTFILE].dat
```

where SCALE is a number from 1 to 7.

It opens up a synthesizer for you whose base note is `C[SCALE]`.
For example, if SCALE is 4, then the base note is `C4`.

The notes you play will be output to OUTPUTFILE.dat file.

### Controls

The keymappings are as follows:

```
a -> C
	w -> C#
s -> D
	e -> D#
d -> E
f -> F
	t -> F#
g -> G
	y -> G#
h -> A
	u -> A#
j -> B
k -> C'

space -> bass sound (set at G1)
any other key -> silence
```

The default duration for each note is fixed at 0.25s.

### Converting to .wav file

The generated OUTPUTFILE.dat can be compiled to a .wav file.
Just run:

```sh
python compile.py [OUTPUTFILE].dat [SOUNDOUTPUTFILE].wav
```

## Contributing

If you like the effort, do consider contributing.

Hack the package as much as you want, raise issues and send PRs.




