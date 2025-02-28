import requests

ESP_IP = "http://192.168.1.100"  # Ganti dengan IP ESP8266 Anda

def kontrol_lampu(perintah):
    url = f"{ESP_IP}/{perintah}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Gagal mengontrol lampu:", response.text)
    except Exception as e:
        print("Error:", e)

kontrol_lampu("lampu_on")  # Menyalakan lampu