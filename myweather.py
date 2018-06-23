import pyowm
from googletrans import Translator
owm = pyowm.OWM('a3ac1a7d13422b804a326029769907f2')
translator = Translator()
def common(city):
    global observation,weather,status,temperature,wind_speed,humidity,pressure
    observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    status = translator.translate(weather.get_status(), dest='vi')
    temperature = weather.get_temperature('celsius')['temp']
    wind_speed = weather.get_wind()['speed']
    humidity = weather.get_humidity()
    pressure = weather.get_pressure()['press']

def completeWeather(city):
    try:
        global wind_speed,status,temperature,humidity,pressure
        common(city)
        print("Thời tiết tại "+city+" là "+status.text+" với nhiệt độ "+str(temperature)+" độ C, "+"tốc độ gió "+str(wind_speed)+" m/s, "+"độ ẩm "+str(humidity)+" %"+" và áp suất "+str(pressure)+" atm.\n")
        return "Thời tiết tại "+city+" là "+status.text+" với nhiệt độ "+str(temperature)+" độ C, "+"tốc độ gió "+str(wind_speed)+" mét trên giây, "+"độ ẩm "+str(humidity)+" %"+" và áp suất "+str(pressure)+" atmosphere."
    except :
        print("Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại.\n")
        return "Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại."

def statusWeather(city):
    try:
        global status
        common(city)
        print("Thời tiết tại "+city+" là "+status.text +".\n")
        return "Thời tiết tại "+city+" là "+status.text
    except :
        print("Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại.\n")
        return "Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại."

def tempWeather(city):
    try:
        global temperature
        common(city)
        print("Nhiệt độ tại "+city+" là "+str(temperature)+" độ C.\n")
        return "Nhiệt độ tại "+city+" là "+str(temperature)+" độ C"
    except :
        print("Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại.\n")
        return "Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại."

def wspeedWeather(city):
    try:
        global wind_speed
        common(city)
        print("Tốc độ gió tại "+city+" là "+str(wind_speed)+" m/s.\n")
        return "Tốc độ gió tại "+city+" là "+str(wind_speed)+" mét trên giây"
    except :
        print("Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại.\n")
        return "Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại."

def humidityWeather(city):
    try:
        global humidity
        common(city)
        print("Độ ẩm tại "+city+" là "+str(humidity)+"%.\n")
        return "Độ ẩm tại "+city+" là "+str(humidity)+"%"
    except :
        print("Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại.\n")
        return "Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại."

def pressureWeather(city):
    try:
        global pressure
        common(city)
        print("Áp suất tại "+city+" là "+str(pressure)+" Atm.\n")
        return "Áp suất tại "+city+" là "+str(pressure)+" Atmosphere."
    except :
        print("Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại.\n")
        return "Không thể dự báo được thời tiết thành phố này. Bạn nên xem xét lại."
