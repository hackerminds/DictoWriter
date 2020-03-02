import os
import time
import threading
import s2t_v4 as s2t
import serial
import time
"sending PYTHON 2 CODE ported to py3"
# Open grbl serial port
s = serial.Serial('/dev/ttyACM1',115200)
#buffer = "welcome to project dicto-writer 1.0"
buffer = " "
oneline = 30
scale = 0.3 # goes well with line yoffset drop of 10
cmd = "./h2g/src/hf2gcode" # ./prog -params "text"
gcd_file = "write.txt"
current_line = 40

from collections import deque
plotter_queue = []
plotter_queue = deque(plotter_queue)



def gc_sender(newgcode):
    # Open g-code file
    f = newgcode
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
    #f.close()
    #s.close()    

    # -----

# s2t.energy_threshold = 2000


def speech_recog():
    while(len(buffer) <= 30):
        new_msg = input("write something:")
        buffer + new_msg

def gen_gcode(mesg,x,y):
    # print(scale)
    print("generating GCODE")
    x,y = str(x),str(y)
    sca = str(scale)
    bashout = cmd +" -m -o " +gcd_file+" --scale "+sca+" -x "+ x +" -y "+ y + " " + "\"" +mesg +"\""
    # bashout = cmd +" --scale "+sca+" -x "+ x +" -y "+ y + " " + "\"" +mesg +"\""
    # print(bashout)
    return os.system(bashout)

def run_plotter(filename):
    print("Plotter is writing :\n"+buffer)
    # cmd2 = "gcd -c v3.json -f write.txt"
    
    

## need to use one thread to fill the buffer by speech recognition
# speech_t = threading.Thread(target = speech_recog)
# speech_t.start()

" thread to control plotter queue "
threading.Thread(target=run_plotter,deamon=True).start()

def main():
    while(True):
        if(len(buffer) >= oneline):
            gen_gcode(buffer[:oneline],0,current_line) #text , xoffset , yoffset
            current_line -= 10 #step down a line
            run_plotter("write.txt") # pass the gcode
            buffer = buffer[oneline:] #retain remaining buffer text
        # speech_recog()
        #time.sleep(0.5) # simply
        #buffer += input("fill buffer :") # fills buffer using user input
        voice = s2t.recog()
        if voice is not None:
            buffer += voice # 

if __name__ == "__main__":
    main()