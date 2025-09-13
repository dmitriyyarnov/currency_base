from pathlib import Path
import pandas as pd
import sys

# Абсолютный путь к папке с CSV
RAW = Path(r"C:/Users/dmitr/PycharmProjects/PythonProject2/data/raw")
ARTIFACTS = Path(r"C:/Users/dmitr/PycharmProjects/PythonProject2/artifacts/plots")
ARTIFACTS.mkdir(parents=True, exist_ok=True)

# Проверяем наличие CSV
files = sorted(RAW.glob("*.csv"))
if not files:
    print("CSV не найден! Проверьте путь:", RAW)
    sys.exit(1)

# Берём последний CSV
df = pd.read_csv(files[-1])

# Фильтруем только нужные валюты
df = df[df['CharCode'].isin(['USD','EUR'])]

# Строим график
import matplotlib.pyplot as plt

plt.figure()
plt.plot(df['CharCode'], df['Value'], marker='o')
plt.title('Курс USD и EUR')
plt.ylabel('RUB')
plt.grid(True)
plt.savefig(ARTIFACTS / 'usd_eur_last14days.png')
print('График сохранён в', ARTIFACTS)