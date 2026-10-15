import csv
import requests
from bs4 import BeautifulSoup

# URL target web tugas
url = "https://chomsky.info/audionvideo/"
response = requests.get(url)

if response.status_code == 200:
    print("Berhasil terhubung ke website!")
    
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("li")
    
    # Simpan langsung ke file CSV
    with open("hasil_tugas.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Judul_Data"])  # Header kolom
        
        for item in titles:
            teks = item.get_text(strip=True)
            if teks:
                writer.writerow([teks])
                
    print("\nSelesai! File 'hasil_tugas.csv' berhasil dibuat!")
else:
    print(f"Gagal terhubung. Status code: {response.status_code}")