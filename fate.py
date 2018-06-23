import speech_recognition
import time
import mytime
import datetime
import myapps 
import gsearch
import mywiki
import myweather
import mymusic
import mylocation
import googletrans
from pygame import mixer
from gtts import gTTS
import os

def say(text):
    source_file = "voice.mp3"
    tts = gTTS(text=text, lang='vi')
    tts.save(source_file)
    mixer.init()
    mixer.music.load(source_file)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    time.sleep(1)
    mixer.music.load("tam.mp3")

speech_identifier = speech_recognition.Recognizer()

def phrase():

        with speech_recognition.Microphone() as source:
                speech_identifier.adjust_for_ambient_noise(source)
                audio = speech_identifier.listen(source)
        try:
                return speech_identifier.recognize_google(audio,language='vi')
        except speech_recognition.UnknownValueError:
                print("Đang chờ sếp ra lệnh.")
        return ""

now = datetime.datetime.now()
hr=now.hour
i = 0
k = 0
guest = "nói chào "

say("3   2   1")
print("\n#####FATE $TART#####\n")

if hr < 12:
    print("Chào buổi sáng. Chúc my fen có một ngày vui vẻ.\n")
    say("Chào buổi sáng. Chúc mai fen có một ngày vui vẻ")
elif hr >= 12 and hr < 17:
    print("Buổi chiều vui vẻ nhé my fen.\n")
    say("Buổi chiều vui vẻ nhé mai fen")
elif hr >= 17 and hr <= 19:
    print("Buổi tối vui vẻ nhé my fen.\n")
    say("Buổi tối vui vẻ nhé mai fen")

while 1:
        str=phrase().lower()
        print (str)
        if str == "hello" or str == "hi" or str == "chào" or str == "xin chào":
            print("Chào my fen. Không biết my fen tên gì.\n")
            say("Chào mai fen. Không biết mai fen tên gì")
            i = 1

        elif str.find("tên")!=-1 or str.find("là")!=-1 and i == 1:
            global j
            i=0
            j = str[str.rindex(" ")+1:]
            print("Chào {}. Lâu quá không gặp.\n".format(j))
            say("Chào {}. Lâu quá không gặp".format(j))

        elif str.find("láo")!=-1 or str.find("xạo")!=-1 or str.find("điêu")!=-1:
            print("Oan cho mình quá.\n")
            say("Oan cho mình quá.")

        elif str.find("giới thiệu")!= -1 and str.find("mình")!=-1:
            print("Xin chào mọi người. Tự giới thiệu, mình tên là Fate. Rất hân hạnh được phục vụ my fen.\n")
            say("Xin chào mọi người. Tự giới thiệu, mình tên là Fate. Rất hân hạnh được phục vụ mai fen. ")

        elif str.find("có ở đó")!=-1:
            print("Ai kêu em đó, có em đây. Em sẽ có mặt trong vòng 3 nốt nhạc. \n")
            say("Ai kêu em đó, có em đây.Em sẽ có mặt trong vòng 3 nốt nhạc. ")

        elif str.find("lâu")!=-1:
            print("Máy cùi bắp. Ram 4 GB, xài 3 năm rồi thì sao chạy nhanh được.\n")
            say("Máy cùi bắp. Ram 4 GB, xài 3 năm rồi thì sao chạy nhanh được ")

        elif str.find("mấy giờ")!=-1 or str.find("ngày mấy")!=-1 or str.find("tháng mấy")!=-1 or str.find("năm mấy")!=-1 \
        or str.find("thứ mấy")!=-1  :
            print("Bây giờ là " + mytime.date_vn +"\n")
            say("Bây giờ là " + mytime.date_vn)

        elif str == "bye" or str == "buy" or str == "break" or str == "kết thúc":
            if hr >= 20 and hr <=24:
                print("Chúc bạn ngủ ngon.\n")
                say("Chúc bạn ngủ ngon")
            else:
                print("Hẹn gặp lại.\n")
                say("Hẹn gặp lại")
            break

        elif str.find("tốt") != -1 or str.find("khỏe") !=-1:
            k = 1
            print("Mình ổn. Còn bạn thì sao?\n")
            say("Mình ổn. Còn bạn thì sao?")

        elif k ==1:
            print("Hỏi vậy thôi chứ mình không quan tâm.\n")
            say("Hỏi vậy thôi chứ mình không quan tâm")
            k =0

        elif str == guest+str[9:]: 
            print("Chào  "+str[9:] +"\n")
            say("Chào "+str[9:])

        elif str.find("google")!= -1:
            print("Vừng ơi mở ra.\n")
            say("Vừng ơi mở ra.")
            gsearch.search(str[str.find("từ")+2:])

        elif str.find("wikipedia")!= -1 or (str.find("cho")!=-1 and str.find("biết")!=-1) :
            say("Chờ xíu.")
            data = mywiki.wiki(str[str.find("về")+2:])
            print (data+"\n")
            say(data)

        elif str.find("là ai")!= -1 :
            print("Đang tìm kiếm thông tin.")
            say("Đang tìm kiếm thông tin.")
            data = mywiki.wiki(str[:str.find("là")])
            print (data+"\n")
            say(data)

        elif str.find("là cái gì")!= -1 or str.find("định nghĩa về")!= -1 :
            print("Đang tìm kiếm thông tin.")
            say("Đang tìm kiếm thông tin.")
            if str.find("là cái gì")!= -1:
                data = mywiki.wiki(str[:str.rfind("là")])
            if str.find("định nghĩa về")!= -1 :
                data = mywiki.wiki(str[str.find("về")+2:])
            print (data+"\n")
            say(data)

        elif str.find("dự báo thời tiết")!= -1  :
            print("Đang tiến hành thu thập thông tin.")
            say("Đang tiến hành thu thập thông tin.")
            report = myweather.completeWeather(str[str.find("tại")+4:])
            say(report)

        elif str.find("địa chỉ") != -1:
            print("Đang xử lí. Vui lòng chờ vài giây!!!")
            say("Đang xử lí. Vui lòng chờ vài giây.")
            print(mylocation.get_location() + "\n")
            say(mylocation.get_location())

        elif str == "mở máy tính":
            say("Đang mở máy tính")
            myapps.calc()

        elif str == "mở excel":
            say("Đang mở")
            myapps.msexcel()

        elif str == "vẽ":
            say("Oke men")
            myapps.mspaint()
        
        elif str.find("bật nhạc") != -1  or str.find("chơi nhạc") != -1 or str.find("mở nhạc") != -1:
            if str.find("đừng") == -1 or str.find("không") == -1 :
                say("Đang bật")
                mymusic.playsong()

        elif str.find("dừng") != -1 or str.find("dừng nhạc") != -1 :
            say("Tạm dừng. Mà đã dừng thì khỏi bật lại")
            mymusic.pausesong()

        elif str.find("tắt") != -1 or str.find("tắt nhạc") != -1:
            say("Đang tắt. Lần sau không nghe hết bài thì đừng có bật.")
            mymusic.stopsong()

        elif str != "":
            print("Chức năng này tạm thời chưa được cài đặt. Hãy chờ phiên bản sau.\n")
            say("Chức năng này tạm thời chưa được cài đặt. Hãy chờ phiên bản sau.")
