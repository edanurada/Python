import instagram2 as pc
from instabot import Bot
import time

# Instagram bot giriş bilgileri
username = "kullanıcı_adınız"
password = "şifreniz"

# Instagram bot nesnesini oluştur
bot = Bot()

try:
    # Botu giriş yapmadan önce başlat
    bot.login(username=username, password=password)
    time.sleep(600)  # 10 dakika bekleme süresi

except KeyboardInterrupt:
    # Kullanıcı Ctrl+C ile işlemi durdurursa
    pass
finally:
    # Bot çıkış yap
    bot.logout()
