import requests

# Thingspeak API anahtarının ve kanal numarasının girildiği yer
api_key = 'api_key'
channel_id = 'channel_id'

# Thingspeak Read API URL'si oluşturulur
thingspeak_url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}'
# &results={"3"} === kaç verinin gösterileceğini yazar

# Veriyi çek
response = requests.get(thingspeak_url)

#durum kodu kontrol edilir
if response.status_code == 200:
    # JSON verisini alın
    json_data = response.json()
    
    # Veriyi yazdır
    for entry in json_data['feeds']:
        field1_value = entry['field1']
        # İlgili verileri almak için diğer 'field' değerlerini de kullanabilirsiniz.
        # 31 kırmızı rengin ANSI kodudur arka plan için 45 gibi 4 ile başlayan sayılar
        print("\033[41m" + "veri = " + "\033[0m" + field1_value)
else:
    print("Veri çekme hatası! Hata kodu:", response.status_code)

