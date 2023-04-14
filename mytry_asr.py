# 2152216 蒋钰萱
from PyQt5 import QtWidgets, QtGui, QtCore, uic
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.uic import loadUiType
from asrInterface import Ui_MainWindow
from guessTheWord import recognize_speech_from_mic
import sys
import os
from os import startfile
import keyboard
import speech_recognition as sr
import win32com.client as win
from pygame import mixer
import time
import os.path
from moviepy.editor import VideoFileClip

# def get_lens(path):
#     files =  [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp4')]
#     times = 0
#     for f in files:
#         # print(f)
#         clip = VideoFileClip(f)
#         # 计算视频的时长，单位为分钟
#         len = f, round(clip.duration/60, 0)
#         times+=len
#         clip.close()
#     return times

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        # 实例化类，用来创建窗口
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def playMusic():
    # os.system(r"C:\Users\深归\Music\Of_Course.mp3")
    # timeStart = time.perf_counter()

    mixer.init()
    mixer.music.load("Of_Course.mp3")
    mixer.music.play()

    # timeEnd = time.perf_counter()
    # duration = timeEnd - timeStart
    # return duration

    # if keyboard.is_pressed('q'):
    #     time.sleep(3)
    #     mixer.music.stop()
    # else:
    #     time.sleep(5)
    #     mixer.music.stop()



def playVideo():
    # startfile(r"D:\UpupooWallpaper\2000308532\video_2000308532.mp4")
    os.system('video_2000308532.mp4')

def openFile():
    os.system('notepad.exe')

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
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("About to stop")
            return

        # if 'and' or 'i' in guess["transcription"]:
        #     speak = win.Dispatch("SAPI.SpVoice")
        #     speak.Speak("About to play music")
        #     playMusic()
        #
        #     seconds = input()
        #     mixer.music.stop()
        if 'think' in guess["transcription"]:
        # if guess["transcription"] == 'play music':
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("About to play music")
            playMusic()
            # 音乐仍然在进行，但麦克风直接读取下一条命令
            # 故采用以下代码解决此问题
            # 输入任意键音乐暂停播放，麦克风读取下一条命令
            seconds = input()
            mixer.music.stop()
        elif 'deal' in guess["transcription"]:
        # elif guess["transcription"] == 'play video':
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("About to play video")
            playVideo()
            time.sleep(5)
        elif 'oh' in guess["transcription"]:
        # elif guess["transcription"] == 'open file':
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("About to open file")
            openFile()
        else:
            myWindow.ui.words("Sorry, I didn't catch that.")
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("Sorry, I didn't catch that.")

# class mainToRun():
#     # 主要运行过程及各函数调用
#     def __init__(self, appWin):
#         self.appWin=appWin
#
#     def myMain(self):
#         guess=get_mic(self.appWin)
#         if(guess=='play the music'):
#             playMusic()
#         if(guess=='play the video'):
#             playVideo()
#         if(guess=='open notepad'):
#              openFile()


# 定义后台线程类myThread
class myThread(QThread):
    # 通过类成员对象定义信号对象
    # 把线程类的信号update_date连接到槽函数
    # 这样后台线程每发射一次信号，就可以把最新的时间值实时显示在前台窗口
    # update_date = pyqtSignal(str)

    def __init__(self, myWindow):
        super(myThread, self).__init__()
        self.myWindow = myWindow

    def run(self):
        get_mic(self.myWindow)
        # 以下无法运行，统一放到get_mic()中处理发现运行通过
        # 猜测可能的原因是sr.Recognizer()和sr.Microphone()不能循环重复调用
        # while True:
        #     guess = get_mic(self.myWindow)
        #     if(guess=='stop'):
        #         break
        #
        #     if(guess=='play the music'):
        #         speak = win.Dispatch("SAPI.SpVoice")
        #         speak.Speak("About to play music")
        #         playMusic()
        #     elif(guess=='play the video'):
        #         speak = win.Dispatch("SAPI.SpVoice")
        #         speak.Speak("About to play video")
        #         playVideo()
        #     elif(guess=='open notepad'):
        #         speak = win.Dispatch("SAPI.SpVoice")
        #         speak.Speak("About to open file")
        #         openFile()
        #     else:
        #         myWindow.ui.words("Sorry, I didn't catch that.")
        #         speak = win.Dispatch("SAPI.SpVoice")
        #         speak.Speak("Sorry, I didn't catch that.")


if __name__ == '__main__':

    # 不能正确显示（文字不能完全显示出来）的解决
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # 实例化了一个应用程序对象QApplication()
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()

    # 直接调用，出现窗口要等说话说完了才能出现的情况
    # 解决方案：尝试多线程处理
    # run=mainToRun(application)
    # run.myMain()

    appThread=myThread(application)
    appThread.start()
    sys.exit(app.exec())