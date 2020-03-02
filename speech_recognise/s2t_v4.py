import time #becoxz i like time
import speech_recognition as sr # to recognize specch
import pyaudio

energy_threshold = 1000
sample_rate = 44100
chunk_size = 512

r = sr.Recognizer()
r.energy_threshold = energy_threshold # amplitude level to pick up 

def recog():
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source: #instance and chunck size to remove clicking sound
        print("Waiting to be called on")
        audio = r.listen(source)
        with open("sample.wav",'wb') as sample:
            sample.write(audio.get_wav_data())
        print("uploading...")

    try:
        return(r.recognize_google(audio))
    except LookupError:             # speech is unintelligible
        print("speech is unintelligible")
        return None
    except sr.UnknownValueError:
        print("sari bagal mare!")
        return None
    except sr.RequestError as e:
        print("{0}".format(e))
        return None
    except:
        print("sari bagal mare!")
        return None

def recog_to_file(fname):
    print("Writing to file: "+fname)
    newmsg = recog()
    if newmsg is not None:
        with open(fname,'a') as txtf:
            txtf.write(newmsg+" ")

def main():
    while True:
        recog_to_file("recogtxt.txt")
        
if __name__ == "__main__":
    main() 

        
            
            
    
