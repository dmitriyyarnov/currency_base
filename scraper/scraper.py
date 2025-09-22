import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

def fetch_usd_rate():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    usd = soup.find("Valute", ID="R01235")
    rate = float(usd.Value.text.replace(",", "."))
    date_str = soup.find("ValCurs")["Date"]
    date_obj = datetime.strptime(date_str, "%d.%m.%Y").date()
    return date_obj.isoformat(), rate

def save_rate(date_str, rate):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    file_path = os.path.join(DATA_FOLDER, f"{date_str}.json")
    with open(file_path, "w") as f:
        json.dump({"date": date_str, "rate": rate}, f)

def run_scraper():
    date_str, rate = fetch_usd_rate()
    save_rate(date_str, rate)
    print(f"Saved USD rate: {rate} on {date_str}")

if __name__ == "__main__":
    run_scraper()



