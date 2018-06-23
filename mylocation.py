import requests
import json

def get_location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    province = j['region_name']
    city = j['city']
    vido = j['latitude']
    kinhdo = j['longitude']
    return "Bạn đang ở tại " + province + ", thành phố "+ city + ", "+ str(vido) + " độ vĩ Bắc, " + str(kinhdo) + " độ kinh Đông."
