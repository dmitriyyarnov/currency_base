from prefect import flow, task
from scraper.scraper import run_scraper

@task
def fetch_and_save():
    run_scraper()

@flow(name="USD Scraper Flow")
def usd_scraper_flow():
    fetch_and_save()

if __name__ == "__main__":
    usd_scraper_flow()
