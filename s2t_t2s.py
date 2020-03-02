import os
import time
import playsound
from gtts import gTTS
import s2t_t2s_rec as s2t #s2t file only used here

speech_mode = False
ttsfeedback = False

#buff = "welcome to project dicto-writer 1.0"
buff = " "
oneline = 20  # characters that can be writen in a line
current_line = 0
plotter_queue = []

def main():
    global buff
    global current_line
    global oneline

    while True:
        if(len(buff) >= oneline):
            offset_txt = None
            #check for the first space from the end of buff
            if buff[oneline-1] == " " or buff[oneline] == " ": #check current and next lettr is space?
                print_txt = buff[:oneline]
                buff = buff[oneline:]  # retain remaining buff text

            else:
                index = 0
                for i in range(len(buff[:oneline])-1, -1, -1): #check for space from last 
                    index += 1
                    if buff[i] == " ":
                        print_txt = buff[:len(buff[:oneline])-index] #send to gcd conveter
                        buff = buff[oneline-index:]  # retain remaining buff text
                        break
            #wordend = buff.find(' ')
            # linefn = f"{gcd_filename}{current_line}.gc"  # linefilename
            # gen_gcode(print_txt, 0, current_line, linefn)  # text , xoffset , yoffset
            print("printing ->" + print_txt)
            # #gen_gcode will save and store gcode for each line in a new file

            # plotter_queue.append(linefn)

            # current_line -= line_drop  # step down a line

            #buff = ' ' +buff[oneline:]  # retain remaining buff text

            print("-->" + buff)

        else:
            if not speech_mode:
                newtext = input("enter text:")+" "
                playBack(newtext)

                if newtext is not None:
                    buff += newtext  # append into buff

            else:
                newtext = s2t.recog()
                print("You said:", newtext)
                playBack(newtext)

                if newtext is not None:
                    buff += ' '+newtext  # append into buff

#allows user to listen to recognized audio using tts
def playBack(newtext):
    if ttsfeedback and newtext is not None:
        fbaud = gTTS(newtext)
        fbaud.save("s2t_t2s.wav")
        # os.system("omxplayer s2t_t2s.mp3") #play at rasperry Pi
        playsound.playsound('s2t_t2s.wav', True)
        # if input("Is it correct (y/n):") == 'n':
        #     print("Rejected: ", newtext)
        #     newtext = None
        # else:
        #     pass
    else:
        pass

if __name__ == "__main__":
    main()
