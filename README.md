![https://badgen.net/badge/code%20style/standard/f2a](https://badgen.net/badge/code%20style/standard/f2a)
# DICTO-WRITTER
This project is about building a mechanical prototype of a Speech to Text Plotter able to write on the given solid surface. Also trying to build a speech synthesizer as the feed back system. 

### This is a final-year engineering project undertaken by me and my friends.

## STEP 1: Setting up Google Speech recognition

### To build a speech to text converter using the raspberry pi


### Use a usb microphone 
## or ..
#### Checking Sound card modules:
```sh
pi@raspberrypi:~ $ cat /proc/asound/modules
 1 snd_usb_audio
pi@raspberrypi:~ $ cat /proc/asound/cards
 1 [Device         ]: USB-Audio - USB PnP Sound Device
                      C-Media Electronics Inc. USB PnP Sound Device at usb-3f980000.usb-1.5, full spe
```
#### Configuring ALSA:
We simply need to tell ALSA what our default PCM card index should be and in what order they should be prioritized in the kernel.
```sh
#cat ~/.asoundrc
cat << EOF | tee ~/.asoundrc

pcm.!default {
        type hw
        card 1
}

ctl.!default {
        type hw
        card 1
}
EOF

sudo nano /usr/share/alsa/alsa.conf
```
### then replace:
```sh
#defaults.ctl.card 0
#defaults.pcm.card 0
```
### with:
```sh
defaults.ctl.card 1
defaults.pcm.card 1
```
## STEP 2: TEXT TO CNC CODE(GCODE)

### SOLID WAY:
To use a library that converts text to gcode
FIXED : HF2GCODE IS BEST SOLUTION (CONFIRMED )

## Colab notebook to generate gcode
https://colab.research.google.com/drive/1zbTVsNTEt2G8f_w0fMJnD0CR2OUvcBxd

### Installation
```sh
wget https://github.com/hackerminds/Dicto_Writer/raw/master/hf.zip
unzip hf.zip
cd hf2gcode-master/src
make # COMPILE THE C SOURCE CODE
mv hf2gcode-master h2g # RENAME FOLDER
```
```sh
cd h2g/src
./hf2gcode -font "rowmans" -y 0 -x 0 -o text_to_write.gcd --min-gcode "Welcome to DictoWriter!"
```
#### SOURCE CODE : https://github.com/Andy1978/hf2gcode

### DOESNT WORK ON Pi 3B+
The G-CODE interpreter for Raspberry Pi 3 (it works on older versions, but untested)
Sending the gcode (direct on raspi):

```sh
gcd -c settings.json -f text_to_write.gcd
```
####  SOURCE CODE: https://github.com/pantadeusz/raspigcd

(EXAMPLE:)https://www.hackster.io/news/skip-the-control-board-and-run-your-cnc-stepper-drivers-directly-from-a-raspberry-pi-b5666f403f71

### Gcode Notes
----------------
> **remember** concept of Gcode is moving the pen/tool from one vertice to another.

> Gcode is always read from top to bottom , this process will connect the vertices sequentially (by action of pen)

> For better understanding think of Gcode as concept of relative positioning to origin (0,0)

|code|desc|
|---|---|
|G0 | pen action off or pen writing off
|G1 | pen action on

> **(in case of pen , instead of G , the Z value matters because pen can write as soon as it touches the paper! ,where as, the tool needs to be rotating fast enough to cut through the subject.)**

|code|desc|
|---|---|
|Z0 | pen down or touching paper
|Z1 | pen up

|code|desc|
|---|---|
|X0 Y1|  moves pen to vertice (0,1)
|X0.5 Y4 | moves pen to vertice (0.5,4)

> try this online simulator ( you can copy paste the code below)
> https://ncviewer.com/
> FOR BETTER UNDERSTANDING ( USE HIDE TOOLPATH AFTER POSITION )

|code|desc|
|---|---|
|N |this is just the sequence number or SI. no of instruction
|( )| parenthesis are treated as comments
|I2.0 J3.5| arc from the x and y position


### gcode meaning:
http://www.linuxcnc.org/docs/html/gcode/g-code.html#gcode:g7


# ADDITIONAL CONTENTS (OPT): 

#### TYPES OF GCODE:
Linux cnc gcode is different  https://www.youtube.com/watch?v=171SuRjzNcQ

#### Linux cnc  on raspi
https://www.youtube.com/results?search_query=linuxcnc+on+raspberry+pi+3+

#### Linux cnc docs
http://linuxcnc.org/docs/

#### (topic of  dicsussion on types of gcode)
https://forum.linuxcnc.org/20-g-code/26733-translating-other-g-code-formats-to-ngc 

#### info:
http://wiki.linuxcnc.org/cgi-bin/wiki.pl?Simple_LinuxCNC_G-Code_Generators#Multi_line_Text_Engraving_Software

#### (PYTHON CODE but its linux cnc gcode (dont know how to use) : 
https://github.com/LinuxCNC/simple-gcode-generators/tree/master/engrave-lines

#### (JAVA CODE(just a lil hesitation to use)): https://github.com/misan/gcodeFont

#### ALTERNATIVE WAY ( No more needed ):
Make a python script to scrap web by using python auto web form filling on this site
Service page : https://www.microtechstelladata.com/TextToNCcode.aspx
Trick : https://learn.onemonth.com/automate-web-forms-with-python/

#### UNIVERSAL GCODE SENDER
https://youtu.be/u35L0jGCqFc
