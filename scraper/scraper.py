import requests
import pandas as pd
from datetime import datetime
from pathlib import Path
from io import StringIO

URL = "https://www.cbr.ru/scripts/XML_daily.asp"
DATA_DIR = Path(__file__).resolve().parents[1] / 'data' / 'raw'
DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_rates():
    resp = requests.get(URL)
    resp.encoding = "windows-1251"

    xml_data = StringIO(resp.text)
    df = pd.read_xml(xml_data)

    df = df[['CharCode', 'Nominal', 'Name', 'Value']]
    df['Value'] = df['Value'].str.replace(',', '.').astype(float) / df['Nominal']
    df['date'] = datetime.now().date()
    return df


def save_rates():
    df = get_rates()
    fname = DATA_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.csv"
    df.to_csv(fname, index=False, encoding="utf-8")
    print("Saved", fname)


if __name__ == "__main__":
    save_rates()