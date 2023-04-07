# Lab1-Automatic-Speech-Recognition
This project is a language recognition program based on Python language.In this project, we will recognize the voice input by the user and complete some corresponding actions, such as playing music, etc.
## 1. Preparation
### 1.1 Related Configurations and Python Libraries That Need to be Installed
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
### 1.2 Operating Environment
The development environment for this project is the Windows system, and the Python version used is Python 3.9.
## 2. Brief Introduction
This project uses the Python library PyQt5 based on the graphical programming framework Qt5 to build a graphical interface and uses speech_ Recognition, a third-party library, accesses and reads the voice in the microphone. By recognizing speech, complete the corresponding operations.
## 3. Project Structure
### 3.1 Architecture of an ASR System
![image](https://user-images.githubusercontent.com/126655217/230094301-3ea62f3d-3b20-45f5-b12b-fa5f565331f7.png)
### 3.2 Program Structure
This project mainly consists of several files: asr. py, asrInterface. py, and guessTheWord. py.
The asrInterface.py file is mainly used to implement graphical interfaces.
The guissTheWord.py file is mainly used to recognize speech obtained from microphones.
The asr. py file is mainly used to call various functions and classes.

![image](https://user-images.githubusercontent.com/126655217/230425168-14da0b9a-8859-45c5-884d-546cad2c7b2d.png)
## 4. Main Functions and Code Implementation
Including the main functions, corresponding code implementation, and problems encountered during the experimental process, as well as solutions and methods.
### 4.1 The Function of Playing Music
Pygame is a cross platform Python library that is a set of Python program modules used to develop game software, developed based on the SDL library. Allowing users to create feature rich games and multimedia programs in Python programs, Pygame is a highly portable module that supports multiple operating systems. Pygame includes the processing of images and sounds. The purpose of using pygame in this project is to play music files.

    from pygame import mixer
    def playMusic():
      mixer.init()
      mixer.music.load(r"C:\Users\深归\Music\Of_Course.mp3")
      mixer.music.play()
      # 播放5秒
      # time.sleep(5)
      # mixer.music.stop()
At first, the author used the method `os.system()` in the os module to process audio files, but some issues arose.

The first issue is that MP3 audio files cannot be read and garbled code will be displayed.
The solution is to modify the pycharm configuration.

    File->Settings->Editor->File Encodings
    # 把Global Encoding设置成GBK即可
The second issue is the existence of waiting time. Specifically, after playing the video or turning off the audio software midway, it takes 5 to 10 seconds to continue reading the microphone for the next time. The reason for this situation has not yet been resolved by the author, so the author has switched to using the pygame module to implement this function.

The author imports the mixer object from the pygame package in the program, and uses the `mixer.music.load()` method to load the audio file and the `mixer.music.play()` method to play the audio file.

But there is still a problem. After starting to play music, the program continues to execute without waiting for the music to finish playing (the main process creates a sub process to open a new window, and the main process immediately continues to execute after creating the sub process). To solve this problem, the author uses the following code when calling the function. By entering any key, the music pauses and the microphone reads the next command.

    playMusic()
    # 音乐仍然在进行，但麦克风直接读取下一条命令
    # 故采用以下代码解决此问题
    # 输入任意键音乐暂停播放，麦克风读取下一条命令
    seconds = input()
    mixer.music.stop()
### 4.2 The Function of Playing Video
The author uses the `os.system()` method in the os module to open video files.

    def playVideo():
        # startfile(r"D:\UpupooWallpaper\2000308532\video_2000308532.mp4")
        os.system(r'D:\UpupooWallpaper\2000308532\video_2000308532.mp4')
The author initially used the method `startfile()` in the Python standard library OS to open video files. However, there have also been situations where the main process creates a child process to open a new window and continues execution without waiting for the window to exit. Therefore, the `os.system()` method was used instead, but this issue has not been resolved. So, based on the playback time `times`  of the video file,  `time.sleep (times)`  is used to pause the main process and resume the main process after the video playback is completed.
### 4.3 The function of Opening Notepad
The author uses the `os.system()` method in the os module to open notepad.

    def openFile():
        os.system('notepad.exe')

In terms of method selection, the author has considered the `os.startfile()` method and the `os.system()` method. The `os.system()` method will wait for the notepad window to exit before continuing execution (the main process opens a new window, the original window enters a sleep state, and when the new window is closed, the main process wakes up the original window again). The `os.startfile()` method opens a window and continues execution without waiting for the window to exit (the main process creates a child process to open a new window, and once the child process is created, the main process immediately continues execution). Therefore, after comprehensive consideration, the author has decided to use the `os.system()` method.
### 4.4 Voice Transcription Function Recorded from Microphone
The main function of this method is to transcribe speech from recordings recorded by the "microphone".
This method returns a dictionary containing three keys:

'success': Boolean value indicating whether the API request was successful.

'error': If no error occurred, it is `None` ; otherwise, if the API cannot be accessed or speech cannot be recognized, it is a string containing the error message.

'transcription': If the speech cannot be transcribed, it is `None` , otherwise it is a string containing the transcribed text.

    def recognize_speech_from_mic(recognizer, microphone):
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_sphinx(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response
### 4.5 Implement Voice Input and Recognition Functions
This method is used to achieve functions such as playing music, videos, and opening files.
    
    from guessTheWord import recognize_speech_from_mic
    import win32com.client as win
    def get_mic(myWindow):
        # 此函数用于实现播放音乐、视频和打开文件等功能

        while True:

            print('开始说话吧！')
        
            # Working with Microphones
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            # 语音提示开始说话
            speak = win.Dispatch("SAPI.SpVoice")  # 微软语音接口
            speak.Speak("Let's start talking!")

            # 此函数用于实现播放音乐、视频和打开文件等功能
            # Working with Microphones
            myWindow.ui.words("正在说话中.../Speaking...")
            guess = recognize_speech_from_mic(recognizer, microphone)
            print("You said: {}".format(guess["transcription"]))
            myWindow.ui.words("Your conversation: " + guess["transcription"])

            if guess["transcription"] == 'stop':
                return
            if guess["transcription"] == 'play music':
                speak = win.Dispatch("SAPI.SpVoice")
                speak.Speak("About to play music")
                playMusic()
                # 音乐仍然在进行，但麦克风直接读取下一条命令
                # 故采用以下代码解决此问题
                # 输入任意键音乐暂停播放，麦克风读取下一条命令
                seconds = input()
                mixer.music.stop()
            elif guess["transcription"] == 'play video':
                speak = win.Dispatch("SAPI.SpVoice")
                speak.Speak("About to play video")
                playVideo()
                # time.sleep(5)
            elif guess["transcription"] == 'open notepad':
                speak = win.Dispatch("SAPI.SpVoice")
                speak.Speak("About to open file")
                openFile()
            else:
                myWindow.ui.words("Sorry, I didn't catch that.")
                speak = win.Dispatch("SAPI.SpVoice")
                speak.Speak("Sorry, I didn't catch that.")
This method references the `win32com.client` module and the `recognize_speech_from_mic()` method in the `guessTheWord.py` file. The `win32com.client` module is used to provide voice prompts to users.          
### 4.6 Method of Implementing Multithreading
At the beginning, the author did not create multiple threads, so there was a situation where a window could only pop up after speaking when loading the interface. After searching for information, the author found that it is possible to create multiple threads, use the main thread to update the interface, use sub threads to process data in real-time, and finally display the results on the interface. This will solve the problems that occurred before.

    class myThread(QThread):
   
        def __init__(self, myWindow):
            super(myThread, self).__init__()
            self.myWindow = myWindow

        def run(self):
            get_mic(self.myWindow)
            
    # ...
    appThread=myThread(application)
    appThread.start()
### 4.7 Implementation of Graphical Interface
This method is mainly implemented using `PyQt5`, a third-party library.

    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
        
            # ...
        
            # label_5
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(60, 400, 201, 21))    # 设置当前QWidget的显示位置和大小
            font = QtGui.QFont()    # 创建字体对象
            font.setFamily("Calibri")   # 设置字体类型
            font.setPointSize(12)   # 设置文字大小
            self.label_5.setFont(font)  # 设置字体
            self.label_5.setStyleSheet("color: rgb(100, 200, 200);")    # 设置控件的样式(QSS)
            self.label_5.setWordWrap(True)  # 设置Label标签文本换行显示
            self.label_5.setObjectName("label_5")
        
            #...
            
        # ...
        
        def words(self, mywords):
            # 在窗口上显示说的话
            _translate = QtCore.QCoreApplication.translate
            self.label_5.setText(_translate("MainWindow", mywords))  
            
    class myWindow(QtWidgets.QMainWindow):

        def __init__(self):
            # 实例化类，用来创建窗口
            super(myWindow, self).__init__()
            self.myCommand = " "
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            
    # ...
    
    # 不能正确显示（文字不能完全显示出来）的解决
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # 实例化了一个应用程序对象QApplication()
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    
    # ...
    
    sys.exit(app.exec())
The author encountered an issue of incomplete text display when implementing a graphical interface. After consulting the materials, the author successfully solved this problem by adding the code `QtCore. QCoreApplication. setAttribute (QtCore. Qt. AA-EnableHighDpiScaling)`.
## 5. Function Implementation Screenshot
Run the program and a window will appear:

![image](https://user-images.githubusercontent.com/126655217/230517308-d3a6bc05-bac4-4ce3-b996-0c52c946dc3d.png)

The program voice plays "let's start taiking!" and displays:

![image](https://user-images.githubusercontent.com/126655217/230518434-0c954535-4b10-46b8-ad8f-c218f152d0f6.png)

After the user inputs "play music" into the microphone through voice, the program prompts "about to play music" and displays the user's voice input in text on the window. At the same time, the program starts playing music and displays:

![image](https://user-images.githubusercontent.com/126655217/230519244-79c1ec0d-9394-47cb-8bd3-3bbbd0ce7a6d.png)

After the user inputs "play video" into the microphone through voice, the program prompts "about to play video" and displays the user's voice input in text on the window, displaying:

![image](https://user-images.githubusercontent.com/126655217/230518834-057a5c58-f73d-4bbc-b387-9f90c287c2ae.png)
![image](https://user-images.githubusercontent.com/126655217/230518917-7d4d17bd-b645-4d7f-adbf-b6ead6891b85.png)

After the user inputs "open notepad" into the microphone through voice, the program prompts "about to open notepad" and displays the user's voice input in text on the window, displaying:

![image](https://user-images.githubusercontent.com/126655217/230517766-350134f3-f642-4c91-b0fc-3f0a9309343a.png)
![image](https://user-images.githubusercontent.com/126655217/230518037-78b739b4-ad38-4c88-b286-1ecc0f263601.png)

## 6. Accuracy of Speech Recognition
In this experiment, the `SpeedRecognition` module is used for speech recognition. The accuracy of speech recognition is relatively low.

还需要详细说明本实验的语音识别准确性！！！

To improve the accuracy of speech recognition, we can start from the following aspects:

1. Preprocess audio files, such as denoising, reducing sampling rate, etc., to improve speech quality.

2. Use better speech recognition engines, such as Google Cloud Speech to Text, Microsoft Azure Speech Services, etc.

3. Increase the size and diversity of the training dataset to improve the model's generalization ability.

4. Optimize the model architecture and hyperparameter, such as using deeper neural networks, adjusting the learning rate, etc.

After consulting materials, the author learned that there are many methods for training speech models, among which one commonly used method is to use deep learning models, such as convolutional neural networks (CNN), recurrent neural networks (RNN), and long short-term memory networks (LSTM). Specifically, the steps for training a speech model are as follows:

1. Data preprocessing: including data cleaning, feature extraction, data enhancement, etc.

2. Model construction: Select an appropriate deep learning model and initialize parameters.

3. Model training: Train the model using a training dataset and optimize the model.

4. Model evaluation: Use a test dataset to evaluate the model and calculate indicators such as accuracy and recall.

5. Model application: Apply the trained model to actual scenarios.
## 7. Code Modification
Contains modifications to the existing GUI and code.

Modifications to the GUI (added control label_5):

    def setupUi(self, MainWindow):
    
        # ...
    
        # label_5
        self.label_5 = QtWidgets.QLabel(self.centralwidget) #创建label_5控件
        self.label_5.setGeometry(QtCore.QRect(60, 400, 201, 21))    # 设置当前QWidget的显示位置和大小
        font = QtGui.QFont()    # 创建字体对象
        font.setFamily("Calibri")   # 设置字体类型
        font.setPointSize(12)   # 设置文字大小
        self.label_5.setFont(font)  # 设置字体
        self.label_5.setStyleSheet("color: rgb(100, 200, 200);")    # 设置控件的样式(QSS)
        self.label_5.setWordWrap(True)  # 设置Label标签文本换行显示
        self.label_5.setObjectName("label_5")   # 为控件设置一个名称，当作控件的ID来使用。
        
   def words(self, mywords):
        # 在窗口上显示说的话
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", mywords))
Modifications to other code: added three methods for playing music, playing videos, and opening files, and added multithreading processing. (The specific code has been shown before)
## 8. Video of Using Speech Recognition Mini Assistant

