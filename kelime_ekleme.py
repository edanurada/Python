import requests

# ThingSpeak kanalı hakkında bilgiler
channel_id = "channel_id"
write_api_key = "write_api_key"
read_api_key = "read_api_key"
channel_id2 = "channel_id2"
write_api_key2 = "write_api_key2"

# ThingSpeak API URL'leri
read_url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}'
write_url = f'https://api.thingspeak.com/update.json?api_key={write_api_key}'
write_url2 = f'https://api.thingspeak.com/update.json?api_key={write_api_key2}'

def fetch_data_from_channel():
    response = requests.get(read_url)
    data = response.json()
    if "feeds" in data:
        return data["feeds"]
    return []

def check_data_in_channel(data, target_data):
    for entry in data:
        if entry["field1"].lower() == target_data:  # Girilen veriyi küçük harfe çevirerek karşılaştır
            return True
    return False

def add_data_to_channel_primary(data):
    payload = {
        "field1": data,
    }

    response = requests.post(write_url, data=payload)
    if response.status_code == 200:
        print("Veri başarıyla birinci kanala eklendi.")
    else:
        print("Veri eklenirken bir hata oluştu.")

def add_data_to_channel_secondary(data, description):
    payload = {
        "field1": data+" == "+description,
    }

    response = requests.post(write_url2, data=payload)
    if response.status_code == 200:
        print("Veri başarıyla ikinci kanala eklendi.")
    else:
        print("Veri eklenirken bir hata oluştu.")

def main():
    target_data = input("Eklemek istediğiniz veriyi girin: ")
    target_data_lower = target_data.lower()  # Girilen veriyi küçük harfe çevir
    
    existing_data = fetch_data_from_channel()
    
    if check_data_in_channel(existing_data, target_data_lower):  # Girilen veriyi küçük harfe çevirerek kontrol et
        print("Kanal zaten istenen veriyi içeriyor, eklenmedi.")
    else:
        add_data_to_channel_primary(target_data_lower)
        description = input("Açıklama Ekleyin: ")
        add_data_to_channel_secondary(target_data_lower, description)

if __name__ == "__main__":
    main()