"gc_sender function PYTHON 2 CODE ported to python3"

import os
import time
import threading
import s2t_v4 as s2t
import serial
import time

# Open grbl serial port
s = serial.Serial('/dev/ttyACM1',115200)

" buffer is a keyword in python for some reason .."

#buff = "welcome to project dicto-writer 1.0"
buff = " "
oneline = 30 #characters that can be writen in a line
current_line = 0
line_drop = 10
# scale = 0.3 # goes well with line yoffset drop of 10
scale = 0.25 # also tweak yoffset 
cmd = "./h2g/src/hf2gcode" # ./prog -params "text"
gcd_folder = "linegcodes/"
gcd_filename = "line.gc"

os.system(f"mkdir {gcd_folder}")
# s2t.energy_threshold = 2000

from collections import deque
plotter_queue = []
plotter_queue = deque(plotter_queue) # to store pending line.gc filenames 

def stream_gcode(filename):
    # Open g-code file
    f = open(filename,'r')

    # Wake up grbl
    s.write("\r\n\r\n".encode())
    time.sleep(2)   # Wait for grbl to initialize 
    s.flushInput()  # Flush startup text in serial input

    # Stream g-code to grbl
    for line in f:
        l = line.strip() # Strip all EOL characters for consistency
        print('Sending: ' + l)
        ln_cmd = l + '\n'
        s.write(ln_cmd.encode()) # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print(grbl_out.strip())

    # Wait here until grbl is finished to close serial port and file.
    print("finished")

    # Close file and serial port
    f.close()
    s.close() # dont know whether closing and opening of port is required ... might be redundant   

def gen_gcode(mesg,x,y,lineno):
    # print(scale)
    print("Generating gcode for: ",mesg)
    print(f"Writing to {lineno}{gcd_file}")
    x,y,lineno = str(x),str(y),str(lineno)
    sca = str(scale)
    bashout = cmd +" -m -o "+gcd_folder+lineno+gcd_filename+" --scale "+sca+" -x "+ x +" -y "+ y + " " + "\"" +mesg +"\""
    # bashout = cmd +" --scale "+sca+" -x "+ x +" -y "+ y + " " + "\"" +mesg +"\""
    # print(bashout)
    return os.system(bashout)

def run_plotter():
	while True:
		global plotter_queue
		if len(plotter_queue) >= 1:
		    cur_line_file = plotter_queue.popleft() # pop first line ,then second, and so on..
		    print("Plotter is writing :"+cur_line_file) 
		    stream_gcode(f"{linegcodes}{cur_line_file}")
		    # cmd2 = "gcd -c v3.json -f write.txt" #deprecated bcz not working as expected
		else:
			print("No pending gcodes ..")
			time.sleep(2)

" TAKEN CARE BY MAIN THREAD "
## need to use one thread to fill the buffer by speech recognition
# speech_t = threading.Thread(target = speech_recog)
# speech_t.start()
" TAKEN CARE BY MAIN THREAD "

def main():
    while True:
        if(len(buff) >= oneline):
        	linefn = f"{current_line}{gcd_file}" #linefilename
            gen_gcode(buff[:oneline],0,current_line,linefn) #text , xoffset , yoffset 
            #gen_gcode will save and store gcode for each line in a new file
            
            plotter_queue.append(linefn)

            current_line -= line_drop #step down a line
            
            buff = buff[oneline:] # retain remaining buff text
        else:
	        newtext = s2t.recog()
	        if newtext is not None:
	            buff += newtext # append into buff

def plotter_handler():
	" thread to control plotter queue "
	threading.Thread(target=run_plotter,deamon=True).start()

if __name__ == "__main__":
	plotter_handler() # sequentialy serial_stream each new file generated in gcd_folder
	main() #main thread performs continous speech recog and gcode generation
