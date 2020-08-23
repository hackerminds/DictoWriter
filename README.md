https://github.com/hackerminds/DICTO-WRITTER/tree/testing_branch
![https://badgen.net/github/last-commit/hackerminds/DICTO-WRITTER/](https://badgen.net/github/last-commit/hackerminds/DICTO-WRITTER)

# DICTO-WRITTER
This project is about building a mechanical prototype of a Speech to Text Plotter able to write on the given solid surface. Also trying to build a speech synthesizer as the feed back system. 


Install Library
----
 1. SpeechRecognition 3.8.1
    
        sudo pip3 install SpeechRecognition
    
    > *Library for performing speech recognition, with support for several engines and APIs, online and offline.* Also check for other
    > requirments at
    > [https://pypi.org/project/SpeechRecognition/](https://pypi.org/project/SpeechRecognition/)
 2. Install Pyaudio 
    
        sudo pip3 install PyAudio 
        
     ## Install Pyaudio
     ```
        sudo apt-get install portaudio19-dev 
        sudo pip install pyaudio
 
     ```
    
    > If the problem occur during installation pyaudio in raspiberry Pi try this, If
    > your system is not "broken", you may be successful with this sequence:
    > 
    > ```
    > 1. sudo apt-get update 
    > 2. sudo apt-get upgrade 
    > 3. sudo apt-get install portaudio19-dev 
    > 4. sudo pip install pyaudio ```
    > 
    > In general: 1. updates the package list on your system, and 2.
    > upgrades all installed packages. These two steps should usually be
    > done before you install any new packages.
    > 
    > If your system still complains of broken packages and such, try this
    > sequence:
    > 
    > ```
    > 1. sudo apt-get update 
    > 2. sudo apt-get upgrade 
    > 3. sudo apt-get dist-upgrade
    > 4. sudo apt-get install portaudio19-dev 
    > 5. sudo pip install pyaudio 
    > ```
    > 
    > Briefly, the difference between step 2 and step 3 is this:
    > 
    > `sudo apt-get dist-upgrade`  will add & remove packages if necessary,
    > and attempts to deal "intelligently" with changed dependencies.
    > 
    > `sudo apt-get upgrade`  under no circumstances are currently installed
    > packages removed, or packages not already installed retrieved and installed. This may be considered "safer" than  `dist-upgrade`, but not as effective in all cases.
    >
    > [1]reference : [https://raspberrypi.stackexchange.com](https://raspberrypi.stackexchange.com/questions/84666/problem-on-installing-pyaudio-on-raspberry-pi)
 3. Python Serial Port Extension for Win32, OSX, Linux
    
        sudo pip3 install pyserial
 4. Import the tesseract from
    [github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
