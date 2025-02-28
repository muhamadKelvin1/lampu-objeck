
#upload kode ini ke ESP anda


import network
import socket

SSID = "WiFi_SSID"
PASSWORD = "WiFi_PASSWORD"

# Koneksi ke WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Terhubung ke WiFi:", wlan.ifconfig())

# Buat Web Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# Kontrol Lampu
lampu_status = False

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    
    if "/lampu_on" in request:
        lampu_status = True
        response = "Lampu MENYALA"
    elif "/lampu_off" in request:
        lampu_status = False
        response = "Lampu MATI"
    else:
        response = "Perintah tidak dikenali"

    conn.send("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n" + response)
    conn.close()