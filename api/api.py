from fastapi import FastAPI, Query
import os
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

app = FastAPI(title="USD Rates API")

@app.get("/rates")
def get_rates(limit: int = Query(10, ge=1, le=100), sort: str = Query("desc", pattern="^(asc|desc)$")):
    if not os.path.exists(DATA_FOLDER) or len(os.listdir(DATA_FOLDER)) == 0:
        return []

    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".json")]

    files = sorted(files, reverse=(sort=="desc"))
    files = files[:limit]

    result = []
    for file in files:
        with open(os.path.join(DATA_FOLDER, file), "r") as f:
            result.append(json.load(f))
    return result
