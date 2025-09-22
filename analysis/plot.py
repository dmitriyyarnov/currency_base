import os
import json
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

if not os.path.exists(DATA_FOLDER):
    raise FileNotFoundError("Папка data не найдена! Запустите скрапер хотя бы один раз.")

files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith(".json")])

dates, rates = [], []

for file in files:
    with open(os.path.join(DATA_FOLDER, file), "r") as f:
        data = json.load(f)
        dates.append(data["date"])
        rates.append(data["rate"])

plt.plot(dates, rates, marker='o')
plt.xticks(rotation=45)
plt.title("USD Rate Dynamics")
plt.xlabel("Date")
plt.ylabel("Rate")
plt.tight_layout()
plt.show()

