from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# WebDriver'ı başlat
driver = webdriver.Edge()

# Trivago ana sayfasına git
url = 'https://www.trivago.com.tr'
driver.get(url)

# Sayfanın tamamen yüklenmesi için bekleme
time.sleep(5)

try:
    # Arama kutusunu bulun
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-form-destination"]'))
    )
    print("Arama kutusu bulundu.")
    
    # Arama kutusuna "Antalya" yazın
    search_box.clear()
    search_box.send_keys('Antalya')
    print("Arama kutusuna 'Antalya' yazıldı.")
    
    time.sleep(3)

    # Enter tuşuna basarak aramayı gerçekleştirin
    search_box.send_keys(Keys.ENTER)
    print("Enter tuşuna basıldı.")

    # Arama sonuçlarının yüklenmesi için bekleme
    time.sleep(5)

    # "Ara" butonunu bulun ve tıklayın
    ara_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="search-button-with-loader"]'))
    )
    print("Ara butonu bulundu, tıklanacak.")
    ara_button.click()
    print("Ara butonuna tıklandı.")
    time.sleep(10)

    # Otel bilgilerini toplamak için liste oluştur
    otel_listesi = []

    # Belirli sayfa sayısı boyunca veri toplama döngüsü (örneğin, 3 sayfa)
    for sayfa in range(13):
        print(f"{sayfa + 1}. sayfa işleniyor...")

        try:
            # Otel isimlerini ve resimlerini çekin
            otel_isimleri = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, '//span[@itemprop="name"]'))
            )
            otel_resimleri = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, '//img[@itemprop="image"]'))
            )
            print(f"{len(otel_isimleri)} otel ismi bulundu.")
            print(f"{len(otel_resimleri)} otel resmi bulundu.")
        except Exception as e:
            print(f"Otel isimleri veya resimleri çekilirken hata oluştu: {e}")
            break

        # İsimleri ve resim URL'lerini bir listede toplayın
        for isim, resim in zip(otel_isimleri, otel_resimleri):
            otel_listesi.append({
                'isim': isim.text.strip(),
                'resim': resim.get_attribute('src')
            })

        # Sonraki sayfaya geçiş yap
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="next-result-page"]'))
            )
            next_button.click()
            print("Sonraki sayfaya geçiş yapıldı.")
            time.sleep(5)  # Sayfanın tamamen yüklenmesini bekle
        except Exception as e:
            print(f"Sonraki sayfa butonu bulunamadı veya tıklanamadı: {e}")
            break

    # Otel isimlerini ve resim URL'lerini yazdırın
    for otel in otel_listesi:
        print(f"Otel İsmi: {otel['isim']}, Resim URL: {otel['resim']}")

    # Otel isimlerini ve resim URL'lerini bir metin dosyasına yazdırın
    with open("oteller.txt", "w", encoding="utf-8") as dosya:
        for otel in otel_listesi:
            dosya.write(f"Otel İsmi: {otel['isim']}, Resim URL: {otel['resim']}\n")

except Exception as e:
    print(f"Hata: {e}")

finally:
    # Tüm pencereleri kapatmak için pencerelerin listesini alın
    tüm_pencereler = driver.window_handles
    # Ana pencereyi bulun
    ana_pencere = tüm_pencereler[0]
    # Diğer pencereleri döngü ile kapatın (ana pencereyi hariç)
    for pencere in tüm_pencereler[1:]:
        driver.switch_to.window(pencere)
        driver.close()
    # Ana pencereye geçin
    driver.switch_to.window(ana_pencere)
    # Ana pencereyi de kapatın
    driver.close()
