import requests
import schedule
import time
from datetime import datetime

# URL du fichier CSV
url = "https://www.data.gouv.fr/fr/datasets/r/b730bbcf-759b-4f5f-849f-a32edcaf5668"

def download_csv():
    response = requests.get(url)
    if response.status_code == 200:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"/Users/akksel/Documents/ING2/S7/Data Vizualization/Projet/data/velib_data_{timestamp}.csv"

        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print("Failed to download the CSV")

schedule.every().day.at("07:30").do(download_csv)
schedule.every().day.at("09:00").do(download_csv)
schedule.every().day.at("10:04").do(download_csv)
schedule.every().day.at("12:00").do(download_csv)
schedule.every().day.at("16:00").do(download_csv)
schedule.every().day.at("19:00").do(download_csv)
schedule.every().day.at("22:00").do(download_csv)
schedule.every().day.at("01:00").do(download_csv)

while True:
    schedule.run_pending()
    time.sleep(60)  # Attendez 1 minute entre les vérifications
