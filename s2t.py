"""Speech recognition and save it to the file"""
import time 
import speech_recognition as sr
import pyaudio

energy_threshold = 1000
sample_rate = 44100
chunk_size = 512

r = sr.Recognizer()
r.energy_threshold = energy_threshold # amplitude level to pick up 

def recog():
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source: #instance and chunck size to remove clicking sound
        r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Listening...")
        audio = r.listen(source)
        with open("/home/pi/Pictures/hackgr9/sample.wav",'wb') as sample:
            sample.write(audio.get_wav_data())
        print("Uploading...")
    try:
        return(r.recognize_google(audio,language="en-IN"))
    except LookupError:             # speech is unintelligible
        print("speech is unintelligible")
        return None
    except sr.UnknownValueError:
        print("Dont talk nonsense!")
        return None
    except sr.RequestError as e:
        print("{0}".format(e))
        return None
    except:
        print("Dont talk nonsense!")
        return None

def recog_to_file(fname):
    print("Writing to file: "+fname)
    newmsg = recog()
    if newmsg is not None:
        with open(fname,'a') as txtf:
            txtf.write(newmsg+" ")

def main():
    while True:
        recog_to_file("/home/pi/Pictures/hackgr9/recogtxt.txt")
        
if __name__ == "__main__":
    main() 

        
            
            
    
