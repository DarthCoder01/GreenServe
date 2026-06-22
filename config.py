from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("WATTTIME_USERNAME")
PASSWORD = os.getenv("WATTTIME_PASSWORD")
REGION = "CAISO_NORTH"

DIRTY_THRESHOLD = 940
GREEN_THRESHOLD = 920
