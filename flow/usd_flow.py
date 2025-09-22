import schedule
import time
from prefect import flow, task
from scraper.scraper import run_scraper

@task
def fetch_and_save():
    run_scraper()

@flow(name="USD Scraper Flow")
def usd_scraper_flow():
    fetch_and_save()


def run_flow():
    usd_scraper_flow()

# Запуск каждый день в час:мин
schedule.every().day.at("00:35").do(run_flow)

print("Scheduler started...")

# Цикл, чтобы проверять задачи каждую минуту
while True:
    schedule.run_pending()
    time.sleep(60)


