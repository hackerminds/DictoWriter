import os
import time
import threading
import s2t_v4 as s2t

# s2t.energy_threshold = 2000

#buffer = "welcome to project dicto-writer 1.0"
buffer = " "
oneline = 30
scale = 0.3 # goes well with line yoffset drop of 10
cmd = "./h2g/src/hf2gcode" # ./prog -params "text"
gcd_file = "write.txt"
current_line = 40

def speech_recog():
    while(len(buffer) <= 30):
        new_msg = input("write something:")
        buffer + new_msg

def gen_gcode(mesg,x,y):
    # print(scale)
    print("generating GCODE")
    x,y = str(x),str(y)
    sca = str(scale)
    bashout = cmd +" -o " +gcd_file+" --scale "+sca+" -x "+ x +" -y "+ y + " " + "\"" +mesg +"\""
    # bashout = cmd +" --scale "+sca+" -x "+ x +" -y "+ y + " " + "\"" +mesg +"\""
    # print(bashout)
    return os.system(bashout)

def run_plotter(filename):
    print("Plotter is writing :\n"+buffer)
    # cmd2 = "gcd -c v3.json -f write.txt"
    cmd2 = "gcd -c v3.json -f "+filename
    os.system(cmd2)

## need to use one thread to fill the buffer by speech recognition
# speech_t = threading.Thread(target = speech_recog)
# speech_t.start()

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
