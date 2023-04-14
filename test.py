
# import speech_recognition as sr

# Working with audio files
# r = sr.Recognizer()
# speech = sr.AudioFile('f1lcapae.wav')
# with speech as source:
#     audio = r.record(source)
# print(r.recognize_sphinx(audio))

# r = sr.Recognizer()
# mic = sr.Microphone()
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# content = r.recognize_sphinx(audio)
# print(content)

# import os
# print("test more")
# os.system('notepad.exe')  #此处已经设置好了该exe文件的环境变量


# print("test more")
# from os import startfile
# startfile(r"D:\UpupooWallpaper\2000308532\video_2000308532.mp4")

# print("test more")
# from pygame import mixer
# import time
# mixer.init()
# mixer.music.load(r"C:\Users\深归\Music\Of Course.mp3")
# mixer.music.play()
# # 播放5秒
# time.sleep(5)
# mixer.music.stop()

# # wav文件可以，但MP3文件播放失败
import os
# file="f1lcapae.wav"
os.system(r"C:\Users\深归\Music\Of_Course.mp3")

# 只能播放wav文件
# import winsound
# filename = "f1lcapae.wav"
# winsound.PlaySound(filename, winsound.SND_FILENAME)

# from playsound import playsound
# playsound("C:/Users/深归/Music/Of Course.mp3")


# print("开始说话吧")
#
# # Working with Microphones
# mic = sr.Microphone()
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# content = r.recognize_sphinx(audio)
# print(content)
#
# if(content=='play the music'):
#     win32api.ShellExecute(0, 'open', 'C:\\Users\\深归\\Music\\Of Course.mp3', '', '', 1)
# elif(content=='Open a text file'):
#     win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 0)