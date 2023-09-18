import pyautogui

# ------- fare komutları ------

print(pyautogui.position());  # Fare imlecinin ekrandaki konumunu yazdırır
pyautogui.moveTo(0,0,6)  # 6 saniyede fareyi (0,0) noktasına taşır
pyautogui.moveRel(0,0,6)  # Fare imleecini olduğu noktadan 6 saniyede fareyi (0,0) noktasına taşır
pyautogui.click(427,258);  # Ekranda (427,258) noktasına gider ve farede bir defa sol tıklar
pyautogui.doubleClick(427,258); # Ekranda (427,258) noktasına gider ve farede 2 defa sol tıklar
pyautogui.rightClick(427,258); # Ekranda (427,258) noktasına gider ve farede 2 defa sağ tıklar
pyautogui.scroll(-2591); # Farenin tekerleğini bir miktar aşağı kaydırır 
pyautogui.mouseDown(427,258); #  Ekranda (427,258) noktasına basar
pyautogui.mouseUp(427,258);  #  Ekranda (427,258) noktasına basmayı bırakır

# ------- klavye komutları ------

pyautogui.typewrite("Hacktorx",interval=1) # Her karakter arasında 1sn bekleyerek ekrana Hacktorx yazdırır
print(pyautogui.press(["ctrl","a"])); # Klavye tuşlarında basarak ctrl ve a tuşlarına tıklar
pyautogui.hotkey("ctrl","a");  # Klavye tuşlarında basarak ctrl+a kısayolunu çalıştırır
 
# ------ ekran komutları ------

Ekran_goruntusu = pyautogui.screenshot() # Ekran görüntüsü alır
Ekran_goruntusu.save("ekran_görüntü_1") # Ekran görüntüsünü kaydeder 

print(pyautogui.size());  # Ekran boyutunu yazdırır

# ------ mesaj Kutusu işlemleri ------

pyautogui.alert( text="Yine ziyaret etmeyi unutmayınız", title="Hacktorx") # Uyarı mesaj kutusu gösterir
pyautogui.confirm(text="Sevdiniz mi?", title="Hacktorx", buttons=["Evet","Tabii ki"]) # Onay mesaj kutusu gösterir
pyautogui.password(text="şifre", title="Hacktorx", mask="*") # Yazılan metnin karakterlerini "*" olarak gösterir
pyautogui.prompt(text="Düşünceleriniz", title="Hacktorx") #Dışarıdan metin girişi olan mesaj kutusu gösterir

# ------ Diğer Komutlar ------
pyautogui.sleep(3) # Kodun çalışmasını 3sn bekletir
pyautogui.FAILSAFE # Kod çalışırken hata oluşması durumunda kodun çalışmasını durdurur