import os
from pygame import mixer
source_file = "C:\\Users\\vietk\\Downloads\\nguoiay.mp3"
def music():
    mixer.init()
    mixer.music.load(source_file)
    
def playsong():
    music()
    mixer.music.play()
    print("Bắt đầu phát bài hát\n")


def pausesong():
    music()
    mixer.music.pause()
    print("Dừng\n")

def unpausesong():
    music()
    while mixer.music.get_busy() == True:
        mixer.music.unpause()
    print("music is unpaused")

def stopsong():
    music()
    mixer.music.stop()
    print("Thoát bài hát\n")
