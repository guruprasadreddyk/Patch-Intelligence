# src/scheduler/job_scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging
from src.data_collection.vendor_scraper import fetch_vendor_patch_info
from src.data_processing.normalizer import normalize_patch_data

logger = logging.getLogger(__name__)

def scheduled_job():
    logger.info("Starting scheduled data update...")
    patch_data = fetch_vendor_patch_info()
    patch_data = normalize_patch_data(patch_data)
    # Here you can add code to update your graph database with new patch_data
    logger.info("Data update completed.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, 'interval', hours=6)
    scheduler.start()
    logger.info("Scheduler started.")
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler shut down gracefully.")

if __name__ == "__main__":
    start_scheduler()
