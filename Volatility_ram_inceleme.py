#!/usr/bin/env python3

import os

def run_volatility(memory_image, command, grep_file=None):
    """
    Belirtilen bellek görüntü dosyası üzerinde belirtilen komutu çalıştırır.
    """
    # Volatility'nin konumu
    volatility_path = "volatility_path.py"

    # PATH değişkenini güncelle
    os.environ["PATH"] += os.pathsep + os.path.dirname(volatility_path)

    # grep dosyası belirtilmişse
    if grep_file:
        command += f" | grep {grep_file}"

    command = f"python3 {volatility_path} -f {memory_image} {command}"
    os.system(command)

def main():
    """
    Ana fonksiyon.
    """
    # Kullanılacak bellek görüntü dosyası
    memory_image = "memory_image.mem"

    print("Seçenekler:")
    print("1. pslist - Çalışan süreçleri listeler")
    print("2. psscan - Fiziksel bellek üzerinde süreçleri tarar")
    print("3. pstree - Süreçler arasındaki ilişkiyi ağaç yapısı olarak gösterir")
    print("4. dlllist - Bir süreç içinde yüklenen DLL'leri listeler")
    print("5. modules - Kernel modüllerini listeler")
    print("6. filescan - Bellek görüntüsü içinde açık dosyaları taramak için kullanılır")
    print("7. handles - Açık kolları listeler")
    print("8. cmdscan - Komut geçmişini tarar")    
    print("9. svcscan - Hizmetleri listeler")
    print("10. malfind - Zararlı kod aramak için kullanılır. Enjekte edilmiş kod içeren süreç bellek aralıklarını listeler")
    print("11. vadinfo - Virtual Address Descriptor (VAD) bilgilerini listeler")
    print("12. BigPools - Büyük Bellek Havuzlarını listeler")
    print("13. Callbacks - Callback Fonksiyonlarını listeler")
    print("14. Crashinfo - Sistem çökmesi bilgilerini listeler")
    print("15. DeviceTree - Aygıt Ağacını listeler")
    print("16. DriverIrp - Sürücü giriş-çıkış işlemlerini (IRP) listeler")
    print("17. DriverModule - Yüklenen sürücü modüllerini listeler")
    print("18. DriverScan - Sürücüleri taramak için kullanılır")
    print("19. DumpFiles - Bellek görüntüsünden dosyaları çıkarmak için kullanılır")
    print("20. Envars - Ortam değişkenlerini listeler")
    print("21. GetServiceSIDs - Hizmetlerle ilişkilendirilen güvenlik kimliklerini listeler")
    print("22. GetSIDs - Güvenlik kimliklerini listeler")
    print("23. IAT - İçe Aktarma Adres Tablosu (IAT) bilgilerini listeler")
    print("24. Info - Bilgisayar ve işletim sistemi bilgilerini listeler")
    print("25. JobLinks - İş bağlantılarını listeler")
    print("26. LdrModules - Yükleyici modülleri listeler")
    print("27. MBRScan - MBR (Ana Önyükleme Kaydı) tarar")
    print("28. Memmap - Bellek haritasını listeler")
    print("29. ADS - Alternatif veri akışlarını (ADS) tarar")
    print("30. MFTScan - MFT (Ana Dosya Tablosu) tarar")
    print("31. ModScan - Modülleri tarar")
    print("32. MutantScan - Kilit nesnelerini (mutant) tarar")
    print("33. NetScan - Ağ bağlantılarını tarar")
    print("34. NetStat - Ağ istatistiklerini listeler")
    print("35. PoolScanner - Bellek havuzlarını tarar")
    print("36. Privs - İşletim sistemi izinlerini listeler")
    print("37. Certificates - Sertifikatları listeler")
    print("38. HiveList - Kayıt defteri hive'larını listeler")
    print("39. HiveScan - Kayıt defteri taramak için kullanılır")
    print("40. PrintKey - Kayıt defteri anahtarlarını listeler")
    print("41. UserAssist - Kullanıcı etkileşimlerini listeler")
    print("42. Sessions - Oturumları listeler")
    print("43. Skeleton_Key_Check - Skeleton Key Checker'ı çalıştırır")
    print("44. SSDT - Sistem Hizmetleri Tanım Tablosu (SSDT) bilgilerini listeler")
    print("45. Statistics - Bellek istatistiklerini listeler")
    print("46. Strings - Karakter dizilerini tarar")
    print("47. SvcScan - Hizmetleri tarar")
    print("48. SymlinkScan - Sembolik bağlantıları tarar")
    print("49. ThrdScan - İş parçacıklarını (thread) tarar")
    print("50. Passphrase - Parola taraması yapar")
    print("51. VadInfo - VAD (Virtual Address Descriptor) bilgilerini listeler")
    print("52. VadWalk - VAD (Virtual Address Descriptor) ağacını tarama")
    print("53. VadYaraScan - YARA taraması yapar")
    print("54. VerInfo - İşletim sistemi dosya bilgilerini listeler")
    print("55. VirtMap - Bellek haritalaması yapar")

    choice = input("Bir seçenek numarası girin: ")

    if choice not in [str(i) for i in range(1, 60)]:
        print("Geçersiz seçenek numarası.")
        return

    # Seçilen komutu belirle
    commands = {
        "1": "windows.pslist.PsList",
        "2": "windows.psscan.PsScan",
        "3": "windows.pstree.PsTree",
        "4": "windows.dlllist.DllList",
        "5": "windows.modules.Modules",
        "6": "windows.filescan.FileScan",
        "7": "windows.handles.Handles",
        "8": "windows.cmdline.CmdLine",
        "9": "windows.svcscan.SvcScan",
        "10": "windows.malfind.Malfind",
        "11": "windows.vadinfo.VadInfo",
        "12": "windows.bigpools.BigPools",
        "13": "windows.callbacks.Callbacks",
        "14": "windows.crashinfo.Crashinfo",
        "15": "windows.devicetree.DeviceTree",
        "16": "windows.driverirp.DriverIrp",
        "17": "windows.drivermodule.DriverModule",
        "18": "windows.driverscan.DriverScan",
        "19": "windows.dumpfiles.DumpFiles",
        "20": "windows.envars.Envars",
        "21": "windows.getservicesids.GetServiceSIDs",
        "22": "windows.getsids.GetSIDs",
        "23": "windows.iat.IAT",
        "24": "windows.info.Info",
        "25": "windows.joblinks.JobLinks",
        "26": "windows.ldrmodules.LdrModules",
        "27": "windows.mbrscan.MBRScan",
        "28": "windows.memmap.Memmap",
        "29": "windows.mftscan.ADS",
        "30": "windows.mftscan.MFTScan",
        "31": "windows.modscan.ModScan",
        "32": "windows.mutantscan.MutantScan",
        "33": "windows.netscan.NetScan",
        "34": "windows.netstat.NetStat",
        "35": "windows.poolscanner.PoolScanner",
        "36": "windows.privileges.Privs",
        "37": "windows.registry.certificates.Certificates",
        "38": "windows.registry.hivelist.HiveList",
        "39": "windows.registry.hivescan.HiveScan",
        "40": "windows.registry.printkey.PrintKey",
        "41": "windows.registry.userassist.UserAssist",
        "42": "windows.sessions.Sessions",
        "43": "windows.skeleton_key_check.Skeleton_Key_Check",
        "44": "windows.ssdt.SSDT",
        "45": "windows.statistics.Statistics",
        "46": "windows.strings.Strings",
        "47": "windows.svcscan.SvcScan",
        "48": "windows.symlinkscan.SymlinkScan",
        "49": "windows.thrdscan.ThrdScan",
        "50": "windows.truecrypt.Passphrase",
        "51": "windows.vadinfo.VadInfo",
        "52": "windows.vadwalk.VadWalk",
        "53": "windows.vadyarascan.VadYaraScan",
        "54": "windows.verinfo.VerInfo",
        "55": "windows.virtmap.VirtMap",
    }

    command = commands[choice]

    # grep eklenip eklenmeyeceğini sor
    grep_choice = input("Komut sonucunda grep eklemek istiyor musunuz? (evet/hayır): ")

    if grep_choice.lower() == "evet":
        grep_file = input("Hangi dosyayı aramak istiyorsunuz? Dosya adı: ")
        run_volatility(memory_image, command, grep_file=grep_file)
    else:
        run_volatility(memory_image, command)

if __name__ == "__main__":
    main()
