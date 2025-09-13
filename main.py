from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(title="Currency Rates API", version="1.0.0")

# Абсолютный путь к графику USD
PLOT_FILE = Path(r"C:/Users/dmitr/PycharmProjects/PythonProject2/artifacts/plots/usd_last14days.png")

@app.get("/")
def root():
    return {"message": "Currency Rates API is running"}

@app.get("/rates/plot")
def get_plot():
    if not PLOT_FILE.exists():
        return {"error": "График не найден. Сначала запустите analyzer.py"}
    return FileResponse(PLOT_FILE, media_type="image/png", filename="usd_last14days.png")
