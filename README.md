Запуск проекта

Собрать первый курс (создаст data/YYYY-MM-DD.json):

python scraper/scraper.py


Запуск Prefect flow (для автоматического запуска):

python flow/usd_flow.py


Запуск API:

uvicorn api.api:app --reload


Эндпоинт: http://127.0.0.1:8000/rates?limit=5&sort=desc

Построение графика динамики курса:

python analysis/plot.py
