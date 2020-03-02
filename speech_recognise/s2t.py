import pyaudio
import wave
import datetime
import signal
import sys
import os

# run the audio capture and send sound sample processes in parallel
from multiprocessing import Process
# convert speech to text using APIs
import speech_recognition as sr

r = sr.Recognizer()

# CONFIG
CHUNK = 8192 # chunkSize
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 # samplingRate, 4100 needed for Aves sampling. choices=[4000, 8000, 16000, 32000, 44100] :: default 16000
RECORD_SECONDS = 10 # sample length in seconds

storagePath = "/home/pi/Downloads/s2t_storage" # storage on assos_listen device

# write to sd-card
def storeFile(filename,frames):
    #print("start writing file: " + filename)
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("written ---->" + filename)
    recogAud(filename)

# recognize the Audio
def recogAud(filename):
    print("\n"+filename)
    with sr.AudioFile(filename) as source: # use the audio source
        audio = r.record(source)  # extract audio data from the file
        try:
            print(r.recognize_google(audio))   # recognize speech using Google Speech Recognition
        except LookupError:             # speech is unintelligible
            print(" @^&%!~$* ")
    
# abort the sampling process
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    
    # close stream and pyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    #sys.exit(0)
    
# MAIN FUNCTION
def recordAudio(p, stream):
    sampleNumber = 0
    while (True):
        print("*** recording ***")
        sampleNumber = sampleNumber +1

        frames = []
        startDateTimeStr = datetime.datetime.now().strftime("%Y-%m-%d__%I-%M-%S-%f")
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        fileName =  "s2t_" + startDateTimeStr + ".wav"

        # create a store process to write the file in parallel
        storeProcess = Process(target=storeFile, args=(fileName,frames))
        storeProcess.start()
        
# ENTRYPOINT FROM CONSOLE
if __name__ == '__main__':

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # directory to write and read files from
    os.chdir(storagePath)

    # abort by pressing Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # start recording
    recordAudio(p, stream)

