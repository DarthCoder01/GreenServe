import requests
from requests.auth import HTTPBasicAuth
from config import *

current_carbon = 0

def fetch_current_carbon():

    global current_carbon

    login = requests.get(
        "https://api.watttime.org/login",
        auth=HTTPBasicAuth(
            USERNAME,
            PASSWORD
        )
    )

    token = login.json()["token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://api.watttime.org/v3/forecast",
        headers=headers,
        params={
            "region": REGION,
            "signal_type": "co2_moer"
        }
    )

    data = response.json()["data"]

    first_non_zero = next(
        item["value"]
        for item in data
        if item["value"] > 0
    )

    current_carbon = first_non_zero

    return current_carbon
