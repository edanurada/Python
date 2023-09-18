import requests
import time

def sure():
    
    # ThingSpeak API anahtarının ve kanal numarasının girildiği yer
    api_key = 'api_key'

    with open("iletilmesini istediğiniz dosyanın konumunu yazın", "r") as dosya:
        veri = dosya.read()

    # Thingspeak API URL'si oluşturulur
    thingspeak_url = f'https://api.thingspeak.com/update?api_key={api_key}&field1={veri}'
    
    # veri gönderilir
    response = requests.get(thingspeak_url)
            
    # Durum kodunu kontrol edin
    if response.status_code == 200:
        print("Veri başarıyla gönderildi.")
        # print(response.cookies) # sunucudan gelen çerezleri almak için kullanılır.

    else:
        print("Veri gönderme hatası! Hata kodu:", response.status_code)

while True:
    sure()
    time.sleep(7)  # 3 saniye bekle

