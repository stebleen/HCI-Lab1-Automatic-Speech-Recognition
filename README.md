# Lab1-Automatic-Speech-Recognition
This project is a language recognition program based on Python language.In this project, we will recognize the voice input by the user and complete some corresponding actions, such as playing music, etc.
## 1. Preparation
### 1.1 Related configurations and Python libraries that need to be installed
Install SpeechRecognition

    pip install SpeechRecognition
Install PocketSphinx  

```
# Download right binary library from [.whl file about PocketSphinx](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx)
# Install .whl file in command window using the following command: 
python -m pip install pocketsphinx‑downloaded_wheel.whl
```
Configure Pycharm
```
# Edit pyvenv.cfg in Pycharm and restart Pycharm 
include-system-site-packages = true
```
Install PyAudio
```
# Download right binary library from [.whl file about PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
# Install .whl file in command window using the following command:
python -m pip install PyAudio‑downloaded_wheel.whl
```
Install PyQt5

    pip install PyQt5
Install pywin32(We need to use the win32 module)

    pip install pywin32
Install pygame

    pip install pygame
### 1.2 Operating environment
The development environment for this project is the Windows system, and the Python version used is Python 3.9.
## 2. Brief Introduction
This project uses the Python library PyQt5 based on the graphical programming framework Qt5 to build a graphical interface and uses speech_ Recognition, a third-party library, accesses and reads the voice in the microphone. By recognizing speech, complete the corresponding operations.
## 3. Project Structure
### 3.1 Architecture of an ASR system
![image](https://user-images.githubusercontent.com/126655217/230094301-3ea62f3d-3b20-45f5-b12b-fa5f565331f7.png)
### 3.2 Program structure
This project mainly consists of several files: asr. py, asrInterface. py, and guessTheWord. py.
The asrInterface.py file is mainly used to implement graphical interfaces.
The guissTheWord.py file is mainly used to recognize speech obtained from microphones.
The asr. py file is mainly used to call various functions and classes.
![image](https://user-images.githubusercontent.com/126655217/230109805-de6b7c07-8085-4e8b-bf77-a461620ddf83.png)
## 4. Main functions and code implementation
### 4.1 The function of playing music
Pygame is a cross platform Python library that is a set of Python program modules used to develop game software, developed based on the SDL library. Allowing users to create feature rich games and multimedia programs in Python programs, Pygame is a highly portable module that supports multiple operating systems. Pygame includes the processing of images and sounds. The purpose of using pygame in this project is to play music files.

    from pygame import mixer
    def playMusic():
      mixer.init()
      mixer.music.load(r"C:\Users\深归\Music\Of_Course.mp3")
      mixer.music.play()
      # 播放5秒
      # time.sleep(5)
      # mixer.music.stop()
At first, the author used the function os. system() in the os module to process audio files, but some issues arose.

The first issue is that MP3 audio files cannot be read and garbled code will be displayed.
The solution is to modify the pycharm configuration.

    File->Settings->Editor->File Encodings
    # 把Global Encoding设置成GBK即可
The second issue is the existence of waiting time. Specifically, after playing the video or turning off the audio software midway, it takes 5 to 10 seconds to continue reading the microphone for the next time. The reason for this situation has not yet been resolved by the author, so the author has switched to using the pygame module to implement this function.
### 4.2 The function of playing video



